---
type: section
subject: "[[Differentiable Manifolds]]"
chapter: 6
section: 50
tags: [differentiable-manifolds, math591]
---
← [[§49 Recap꞉ Germs, Derivations and Tangent Vectors]] · ↑ [[· 6 Tangent and Cotangent Bundles]] · [[§51 The Tangent Bundle]] →

*Stage: recap — Covectors, the differential of a function, pullbacks — and the four objects that the course calls “the differential”, side by side.*

*Not from lecture: a recap written for these notes, continuing [[§49 Recap꞉ Germs, Derivations and Tangent Vectors|§49]]. Nothing here is new; every object is defined, and every fact proved, where the cross-reference points.*

Keep one picture in mind: $M$ is a surface, $f$ is the temperature on it, and you are walking on it. A tangent vector is a direction to walk in. This section is about the objects that *eat* directions.

**Step 1: covectors are linear functions on a vector space.** The dual space $V^{\ast}$ of a vector space $V$ consists of the linear maps $V \to \mathbb{R}$, its elements are called *covectors*, and a basis $(e_i)$ of $V$ has a dual basis $(\varepsilon^i)$ with $\varepsilon^i(e_j) = \delta^i_j$ ([[§21 Linear Algebra Toolkit#^def-21-1|Definitions §21.1]] and [[§21 Linear Algebra Toolkit#^def-21-2|§21.2]]). Components come out by evaluation, $\lambda = \sum_i \lambda(e_i)\, \varepsilon^i$ ([[§21 Linear Algebra Toolkit#^prop-21-2|Proposition §21.2]]). A linear map $A : V \to W$ has a dual map $A^{\ast} : W^{\ast} \to V^{\ast}$, $A^{\ast}\lambda = \lambda \circ A$, which goes *backwards* ([[§21 Linear Algebra Toolkit#^def-21-3|Definition §21.3]]).

![[§21 Linear Algebra Toolkit#^def-21-1]]

![[§21 Linear Algebra Toolkit#^def-21-2]]

![[§21 Linear Algebra Toolkit#^def-21-3]]

**Step 2: the cotangent space.** At $p \in M$, $T_p^{\ast}M = (T_pM)^{\ast}$ ([[§32 The Cotangent Space#^def-32-4|Definition §32.4]]). A covector $\alpha \in T_p^{\ast}M$ eats a direction $v \in T_pM$ and returns a number $\alpha(v)$: think of it as a price list for the first step of a walk.

![[§32 The Cotangent Space#^def-32-4]]

**Step 3: a function produces a covector, its differential.** The *differential* of $f$ at $p$ is the covector

$$
df_p \in T_p^*M, \qquad df_p(v) = v[f]
$$

([[§32 The Cotangent Space#^def-32-5|Definition §32.5]] and [[§32 The Cotangent Space#^prop-32-2|Proposition §32.2]]): feed it a direction, and it returns how fast the temperature changes that way. Officially $df_p$ is the pushforward $f_{\ast p} : T_pM \to T_{f(p)}\mathbb{R}$ followed by the identification $T_{f(p)}\mathbb{R} \cong \mathbb{R}$, so it is the differential of Step 5 of [[§49 Recap꞉ Germs, Derivations and Tangent Vectors|§49]] for the special target $N = \mathbb{R}$. In a chart the differentials $dx^i|_p$ of the coordinate functions form the basis dual to $\partial/\partial x^i|_p$, and

$$
df_p = \sum_{i=1}^m \frac{\partial f}{\partial x^i}(p)\, dx^i\big|_p
$$

([[§33 Covectors in Coordinates#^lem-33-1|Lemma §33.1]]); the components of any covector are found by evaluation, $\alpha = \sum_j \alpha(\partial/\partial x^j|_p)\, dx^j|_p$ ([[§33 Covectors in Coordinates#^cor-33-2|Corollary §33.2]]). This is the formula of multivariable calculus, but $df_p$ is *not* the gradient: turning the covector $df_p$ into a vector needs an inner product, which a manifold does not come with ([[§33 Covectors in Coordinates#^rem-33-2|Remark: Differential — Not Gradient]]). In $\mathbb{R}^n$ with the dot product, $df_p(v) = \nabla f(p) \cdot v$.

![[§32 The Cotangent Space#^def-32-5]]

![[§33 Covectors in Coordinates#^lem-33-1]]

![[§33 Covectors in Coordinates#^cor-33-2]]

![[m591-40-1.svg]]
*A covector drawn as a stack of parallel lines. In $\mathbb{R}^2$ (or in one tangent space, after choosing a basis) the covector $\alpha = 2\,dx + dy$ is pictured by its level lines $\{\alpha = 0\}, \{\alpha = 1\}, \ldots$; its value on an arrow is the number of lines the arrow crosses, with sign. $v = \partial_x + \partial_y$ crosses three, so $\alpha(v) = 3$; $w = 0.6\,\partial_x - 1.2\,\partial_y$ runs along the lines, so $\alpha(w) = 0$. For $\alpha = df_p$ the lines are the level sets of the linear approximation of $f$ at $p$: closely spaced lines mean a steep $f$. An arrow and a stack of lines are different kinds of objects; only an inner product turns one into the other.*

**Step 4: the cotangent space from germs alone.** The differential of $f$ depends only on $f$ to first order: $T_p^{\ast}M \cong I_p/I_p^2$, the germs vanishing at $p$ modulo those vanishing to second order, by ${[}[f - f(p)]{]} \mapsto df_p$ ([[§34 The Cotangent Space from Germs#^thm-34-4|Theorem §34.4]]). So covectors can be built from functions without mentioning tangent vectors at all — the cotangent space is “very extremely natural from the point of view of functions” ([[§34 The Cotangent Space from Germs#^rem-34-2|Remark: The Most Natural Description]]).

![[§34 The Cotangent Space from Germs#^def-34-1]]

![[§34 The Cotangent Space from Germs#^thm-34-4]]

**Step 5: covectors pull back.** For $F : M \to N$, the dual map of $F_{\ast p}$ is the *pullback of covectors* $F_p^{\ast} : T^{\ast}_{F(p)}N \to T_p^{\ast}M$, $(F_p^{\ast}\alpha)(v) = \alpha(F_{\ast p}v)$ ([[§34 The Cotangent Space from Germs#^def-34-3|Definition §34.3]]). It commutes with differentials: $F_p^{\ast}(df_{F(p)}) = d(f \circ F)_p$ ([[§34 The Cotangent Space from Germs#^prop-34-6|Proposition §34.6]]), which is the chain rule in covector form. The same symbol $F_p^{\ast}$ already denoted the pullback of germs (Step 5 of [[§49 Recap꞉ Germs, Derivations and Tangent Vectors|§49]]); the two are compatible, as [[§34 The Cotangent Space from Germs#^rem-34-4|Remark: One Symbol for Two Pullbacks]] explains. In charts $(x^1, \ldots, x^m)$ near $p$ and $(y^1, \ldots, y^n)$ near $F(p)$, the matrix of $F_p^{\ast}$ in the dual bases $dy^j|_{F(p)}$ and $dx^i|_p$ is the transpose of the Jacobian of Step 5 of [[§49 Recap꞉ Germs, Derivations and Tangent Vectors|§49]] (Proposition [[§21 Linear Algebra Toolkit#^prop-21-4|§21.4]](2)):

$$
\begin{pmatrix}
\dfrac{\partial F^1}{\partial x^1}(p) & \cdots & \dfrac{\partial F^n}{\partial x^1}(p) \\
\vdots & \ddots & \vdots \\
\dfrac{\partial F^1}{\partial x^m}(p) & \cdots & \dfrac{\partial F^n}{\partial x^m}(p)
\end{pmatrix},
$$

an $m \times n$ matrix whose $j$-th column lists the components of $F_p^{\ast}(dy^j|_{F(p)}) = d(F^j)_p$.

![[§34 The Cotangent Space from Germs#^def-34-3]]

![[§34 The Cotangent Space from Germs#^prop-34-6]]

**Step 6: the word “differential”.** The course uses it for four objects. They are one idea at four levels of generality.

| Name | Symbol | Takes … to … | Defined in |
|---|---|---|---|
| differential of a map between vector spaces | $dF_p$ | a vector in $X$ to a vector in $Y$ (the Jacobian) | [[§22 The Differential of a Map Between Vector Spaces#^def-22-5\|Definition §22.5]] |
| differential (pushforward) of a smooth map | $F_{\ast p}$ | $T_pM \to T_{F(p)}N$ | [[§28 Derivations and the Abstract Tangent Space#^def-28-6\|Definition §28.6]] |
| differential of a function at $p$ | $df_p$ | $T_pM \to \mathbb{R}$, a covector | [[§32 The Cotangent Space#^def-32-5\|Definition §32.5]] |
| the operator $d$ | $d$ | a function $f$ to the one-form $df$ | [[§53 One-Forms#^prop-53-2\|Proposition §53.2]] |

How they fit: on open subsets of $\mathbb{R}^n$ the second is the first ([[§30 The Differential in Coordinates#^prop-30-5|Proposition §30.5]]); Lee writes $dF_p$ for what these notes call $F_{\ast p}$, and Uribe said in Lecture 15 that $F_{\ast p}$ “we should have called the differential of $F$ ages ago”. The third is the second for maps into $\mathbb{R}$. The fourth collects the third over all points: $df$ is the field $p \mapsto df_p$, a one-form ([[§53 One-Forms|§53]]).

**Step 7: forward and backward.** Given $F : M \to N$:

| Object | Moves | Rule |
|---|---|---|
| point $p \in M$ | forward | $p \mapsto F(p)$ |
| tangent vector $v \in T_pM$ | forward | $F_{\ast p}v \in T_{F(p)}N$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-6\|Definition §28.6]]) |
| function $f$ on $N$ | backward | $F^{\ast}f = f \circ F$ on $M$ |
| germ $[g]$ at $F(p)$ | backward | $F_p^{\ast}[g] = [g \circ F]$ ([[§28 Derivations and the Abstract Tangent Space#^def-28-5\|Definition §28.5]]) |
| covector $\alpha \in T^{\ast}_{F(p)}N$ | backward | $(F_p^{\ast}\alpha)(v) = \alpha(F_{\ast p}v)$ ([[§34 The Cotangent Space from Germs#^def-34-3\|Definition §34.3]]) |

Things that *are* somewhere move forward with the points; things that *eat* move backward, because to evaluate one on $M$ you push its input forward and evaluate on $N$.

**What this chapter builds.** So far every object lives at a single point. This chapter lets the point vary. The tangent spaces are assembled into one manifold, the tangent bundle $TM$ ([[§51 The Tangent Bundle|§51]]), and the cotangent spaces into the cotangent bundle $T^{\ast}M$ ([[§52 The Cotangent Bundle|§52]]). A smooth choice of a covector at every point is a one-form; $d$ turns functions into one-forms, and $F^{\ast}$ pulls one-forms back ([[§53 One-Forms|§53]]). The next chapter turns to the sections of $TM$: a smooth choice of a tangent vector at every point is a vector field, and a vector field differentiates functions everywhere at once ([[§56 Vector Fields|§56]]).

> [!example] Example §50.1: Covectors in the Plane
> Continue [[§49 Recap꞉ Germs, Derivations and Tangent Vectors#^ex-49-1|Example §49.1]]: $p = (1, 2)$, $f = x^2 y$, $v = 3\,\partial_x - \partial_y$, and $F(x, y) = (x^2, x + y)$ with $F(p) = (1, 3)$ and $F_{\ast p}v = 6\,\partial_u + 2\,\partial_w$.
> 1. *The differential of $f$.* $df_p = \partial_x f(p)\, dx + \partial_y f(p)\, dy = 4\, dx + dy$, and $df_p(v) = 4 \cdot 3 + 1 \cdot (-1) = 11 = v[f]$, as Step 3 promises.
> 2. *A covector at $F(p)$.* Let $g(u, w) = u w^2$ on the target. Then $dg_{F(p)} = w^2\, du + 2uw\, dw = 9\, du + 6\, dw$ at $(1, 3)$.
> 3. *Its pullback, by definition.* $(F_p^{\ast} dg_{F(p)})(v) = dg_{F(p)}(F_{\ast p}v) = 9 \cdot 6 + 6 \cdot 2 = 66$.
> 4. *Its pullback, by the chain rule.* $g \circ F = x^2 (x + y)^2$, with $\partial_x (g \circ F)(p) = 2x(x+y)^2 + 2x^2(x+y) = 18 + 6 = 24$ and $\partial_y (g \circ F)(p) = 2x^2(x+y) = 6$. So $d(g \circ F)_p = 24\, dx + 6\, dy$, and $d(g \circ F)_p(v) = 72 - 6 = 66$: the two agree, as [[§34 The Cotangent Space from Germs#^prop-34-6|Proposition §34.6]] says.
> 5. *The transpose.* The components of $F_p^{\ast}$ come from the *transpose* of the Jacobian: $\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 9 \\ 6 \end{pmatrix} = \begin{pmatrix} 24 \\ 6 \end{pmatrix}$. Vectors are pushed forward by the Jacobian, covectors pulled back by its transpose.

^ex-50-1

*(Not from lecture; the conversion diagram of the midterm check sheet, added on request.)* The differential of a smooth $F : M \to N$ at $p$, in four equivalent forms. Charts $(U, \varphi = (x^1, \ldots, x^m))$ at $p$ and $(V, \psi = (y^1, \ldots, y^n))$ at $F(p)$, $F^i = y^i \circ F$.

![[m591-48-1.svg]]

*Uses:* [[§33 Covectors in Coordinates#^lem-33-1|§33.1]], [[§34 The Cotangent Space from Germs#^def-34-3|Def. §34.3]], [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]], [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]

> [!remark] Remark: Conversion Diagram for the Differential
> 1. *Germs and curves.* $(F_{\ast p}D)[g] = D[g \circ F]$ (Definition [[§28 Derivations and the Abstract Tangent Space#^def-28-6|§28.6]]); for $D = D_\gamma$, $F_{\ast p}D_\gamma = D_{F \circ \gamma}$, i.e. $F_{\ast}(\gamma'(0)) = (F \circ \gamma)'(0)$ (Corollary [[§31 Tangent Vectors as Velocities of Curves#^cor-31-3|§31.3]]).
> 2. *Germs and the Jacobian.* $F_{\ast p}\big(\partial/\partial x^j|_p\big) = \sum_i \frac{\partial F^i}{\partial x^j}(p)\, \partial/\partial y^i|_{F(p)}$: column $j$ of the Jacobian of $\psi \circ F \circ \varphi^{-1}$ (Theorem [[§30 The Differential in Coordinates#^thm-30-2|§30.2]]); on components, $(F_{\ast p}v)^i = \sum_j \frac{\partial F^i}{\partial x^j}(p)\, v^j$.
> 3. *The Jacobian and the vector-space formula.* Between open subsets of vector spaces, $F_{\ast p}v = \frac{d}{dt}\big|_{t=0} F(p + tv)$ once $F$ is known to be smooth, and any curve with velocity $v$ may replace the line (Theorem [[§22 The Differential of a Map Between Vector Spaces#^thm-22-3|§22.3]], Proposition [[§30 The Differential in Coordinates#^prop-30-5|§30.5]]).
>
> *For a function $f : M \to \mathbb{R}$*, five faces of $df_p \in T_p^{\ast}M$:
>
> $$
> df_p(v) = v[f] = f_{\ast p}(v) = (f \circ \gamma)'(0) = \sum_j \frac{\partial f}{\partial x^j}(p)\, v^j ,
> $$
>
> with $f_{\ast p}(v)$ read through $T_{f(p)}\mathbb{R} \cong \mathbb{R}$ and $\gamma$ any curve with velocity $v$; $df_p = \sum_j \frac{\partial f}{\partial x^j}(p)\, dx^j|_p$ (Lemma [[§33 Covectors in Coordinates#^lem-33-1|§33.1]]); in $\mathbb{R}^n$, $df_p(v) = \nabla f(p) \cdot v$; and, on germs, $df_p$ corresponds to the class of $f - f(p)$ in $I_p/I_p^2$ (Theorem [[§34 The Cotangent Space from Germs#^thm-34-4|§34.4]]).
>
> *Covectors.* Components $\xi_j = \xi(\partial/\partial x^j|_p)$, $\xi = \sum_j \xi_j\, dx^j|_p$ (Corollary [[§33 Covectors in Coordinates#^cor-33-2|§33.2]]); under a change of chart $\xi_i = \sum_j \frac{\partial \tilde x^j}{\partial x^i}(p)\, \tilde\xi_j$, the transpose of the rule for vectors. The pullback $F_p^{\ast}\xi = \xi \circ F_{\ast p}$ has the transposed Jacobian as its matrix (Definition [[§34 The Cotangent Space from Germs#^def-34-3|§34.3]]), and $F_p^{\ast}\big(dg_{F(p)}\big) = d(g \circ F)_p$ (Proposition [[§34 The Cotangent Space from Germs#^prop-34-6|§34.6]]).

^rem-50-1
