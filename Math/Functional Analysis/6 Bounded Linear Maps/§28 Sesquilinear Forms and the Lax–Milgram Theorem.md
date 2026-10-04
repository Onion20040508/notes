---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 28
tags: [functional-analysis, math556]
---
← [[§27 Dual Spaces]] · ↑ [[· 6 Bounded Linear Maps]] · [[§29 ℝⁿ, Cᵐ and Lᵖ]] →

*Stage: maps — Thread: functionals. Bounded sesquilinear forms are bounded operators in disguise; Lax–Milgram extends the Riesz representation to forms that are not symmetric.*

> [!example] Example §28.1: Bilinear Forms on $\mathbb{R}^n$ are Matrices
> Let $B : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ be bilinear (linear in each variable). Then $B(x, y) = (x, Ay)$ for the matrix $A = \bigl( B(e_i, e_j) \bigr)_{i,j}$.

^ex-28-1

> [!proof]+ Proof
> Write $x = \sum_i x_i e_i$, $y = \sum_j y_j e_j$. By bilinearity, $B(x, y) = \sum_{i,j} x_i y_j\, B(e_i, e_j)$. On the other hand $(Ay)_i = \sum_j A_{ij} y_j$, so $(x, Ay) = \sum_i x_i \sum_j A_{ij} y_j = \sum_{i,j} x_i y_j A_{ij}$. The two agree when $A_{ij} = B(e_i, e_j)$.

^pf-ex-28-1

*Uses:* [[§20 Definition and Examples#^ex-20-1|Ex. §20.1]]

> [!remark]- Connections
> - Finite-dimensional home: bilinear forms [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-1|LADR 9.1]], the matrix of a bilinear form [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-4|LADR 9.4]], and forms ↔ matrices as an isomorphism [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-5|LADR 9.5]].

The theorem below is the infinite-dimensional version. Wu warned against the naive route — expanding $x$ and $y$ in an orthonormal basis and building an infinite matrix — because of the ambiguity in such infinite sums; the [[§27 Dual Spaces#^thm-27-2|Riesz representation theorem]] does the work instead.

> [!definition] Definition §28.1: Sesquilinear Form; Bounded Form
> Let $X$ be a linear space over $\mathbb{F}$. A map $B : X \times X \to \mathbb{F}$ is **sesquilinear** if
> - (1) $B(a_1 x_1 + a_2 x_2, y) = a_1 B(x_1, y) + a_2 B(x_2, y)$ for all $a_1, a_2 \in \mathbb{F}$ and $x_1, x_2, y \in X$;
> - (2) $B(x, b_1 y_1 + b_2 y_2) = \overline{b_1}\, B(x, y_1) + \overline{b_2}\, B(x, y_2)$ for all $b_1, b_2 \in \mathbb{F}$ and $x, y_1, y_2 \in X$.
>
> (For $\mathbb{F} = \mathbb{R}$ this is bilinear.) If $X$ is normed, $B$ is **bounded** if there is $M > 0$ with $|B(x, y)| \le M\, \|x\|\, \|y\|$ for all $x, y \in X$.
>
> *Lax: §6.3, conditions (i)–(ii) of Thm 6*

^def-28-1

> [!remark]- Connections
> - An inner product is a sesquilinear form that is also conjugate-symmetric and positive: [[§20 Definition and Examples#^def-20-1|Def. §20.1]]; finite-dimensional home [[§19 Inner Products and Norms#^ladr-6-2|LADR 6.2]].
> - The real case, bilinear forms: [[§32 Bilinear Forms and Quadratic Forms#^ladr-9-1|LADR 9.1]].

> [!theorem] Theorem §28.1: Bounded Sesquilinear Forms are Bounded Operators
> Let $H$ be a Hilbert space over $\mathbb{F}$ and $B : H \times H \to \mathbb{F}$ a bounded sesquilinear form. Then there is a bounded linear map $A : H \to H$ with
>
> $$
> B(x, y) = (x, Ay) \qquad \text{for all } x, y \in H,
> $$
>
> and
>
> $$
> \|A\| = \sup_{\substack{x, y \in H \\ x \neq 0,\ y \neq 0}} \frac{|B(x, y)|}{\|x\|\, \|y\|} .
> $$
>
> *Lax: cf. Ch. 31, Thm 1 (symmetric forms); §6.3, (20)*

^thm-28-1

> [!proof]+ Proof
> **Step 1: defining $A$.** Fix $y_0 \in H$ and let $\ell(x) = B(x, y_0)$. By (1), $\ell$ is linear, and $|\ell(x)| = |B(x, y_0)| \le M\, \|x\|\, \|y_0\|$, so $\ell$ is a bounded linear functional with $\|\ell\| \le M\|y_0\|$. By the [[§27 Dual Spaces#^thm-27-2|Riesz representation theorem]] there is a unique $z_0 \in H$ with
>
> $$
> B(x, y_0) = \ell(x) = (x, z_0) \qquad \text{for all } x \in H .
> $$
>
> Define $A y_0 = z_0$. Doing this for every $y_0$ defines $A : H \to H$, characterized by $B(x, y) = (x, Ay)$ for all $x, y$.
>
> **Step 2: $A$ is linear.** For $a_1, a_2 \in \mathbb{F}$, $y_1, y_2 \in H$ and every $x \in H$,
>
> $$
> \begin{aligned}
> (x, A(a_1 y_1 + a_2 y_2)) &= B(x, a_1 y_1 + a_2 y_2) = \overline{a_1}\, B(x, y_1) + \overline{a_2}\, B(x, y_2) \\
> &= \overline{a_1}\, (x, A y_1) + \overline{a_2}\, (x, A y_2) = (x, a_1 A y_1 + a_2 A y_2),
> \end{aligned}
> $$
>
> by the definition of $A$, property (2) of $B$, the definition of $A$ again, and conjugate-linearity of the inner product.
> Since this holds for every $x$, taking $x = A(a_1 y_1 + a_2 y_2) - (a_1 A y_1 + a_2 A y_2)$ shows that this vector has norm $0$. So $A(a_1 y_1 + a_2 y_2) = a_1 A y_1 + a_2 A y_2$.
>
> **Step 3: $A$ is bounded.** From $|B(x, y)| \le M\|x\|\,\|y\|$, $|(x, Ay)| \le M\, \|x\|\, \|y\|$ for all $x, y$. Take $x = Ay$: $\|Ay\|^2 \le M\, \|Ay\|\, \|y\|$, so $\|Ay\| \le M\|y\|$ (trivially if $Ay = 0$, otherwise divide by $\|Ay\|$). Hence $A$ is bounded with $\|A\| \le M$.
>
> **Step 4: the norm of $A$.**
> (Left to the class in lecture.) Let $S$ denote the supremum in the statement; we may assume $H \neq \{0\}$. For $x, y \neq 0$, [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|Cauchy–Schwarz]] and Proposition [[§26 Boundedness and Continuity#^prop-26-1|§26.1]](b) give $|B(x,y)| = |(x, Ay)| \le \|x\|\,\|Ay\| \le \|A\|\,\|x\|\,\|y\|$, so $S \le \|A\|$. Conversely, for $y \neq 0$ with $Ay \neq 0$, take $x = Ay$: $\dfrac{|B(Ay, y)|}{\|Ay\|\,\|y\|} = \dfrac{\|Ay\|^2}{\|Ay\|\,\|y\|} = \dfrac{\|Ay\|}{\|y\|}$, so $\|Ay\|/\|y\| \le S$; this also holds when $Ay = 0$. Taking the supremum over $y \neq 0$ gives $\|A\| \le S$.

^pf-28-1

*Uses:* [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^def-28-1|Def. §28.1]], [[§27 Dual Spaces#^thm-27-2|§27.2]], [[§20 Definition and Examples#^def-20-1|Def. §20.1]], [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|§21.1]], [[§26 Boundedness and Continuity#^def-26-2|Def. §26.2]], [[§26 Boundedness and Continuity#^prop-26-1|§26.1]]

> [!theorem] Theorem §28.2: Lax–Milgram
> Let $H$ be a Hilbert space over $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$, and let $B : H \times H \to \mathbb{F}$ satisfy
> - (1) $B(a_1 x_1 + a_2 x_2, y) = a_1 B(x_1, y) + a_2 B(x_2, y)$;
> - (2) $B(x, b_1 y_1 + b_2 y_2) = \overline{b_1}\, B(x, y_1) + \overline{b_2}\, B(x, y_2)$;
> - (3) $B$ is bounded: $|B(x, y)| \le M\, \|x\|\, \|y\|$ for all $x, y \in H$;
> - (4) $B$ is **coercive**: there is $\beta > 0$ with $|B(x, x)| \ge \beta\, \|x\|^2$ for all $x \in H$.
>
> Then for every $\ell \in H'$ there is a unique $y \in H$ with
>
> $$
> \ell(x) = B(x, y) \qquad \text{for all } x \in H .
> $$
>
> *Lax: §6.3, Thm 6*

^thm-28-2

> [!proof]+ Proof
> Next lecture.

^pf-28-2

> [!remark] Remark: The Plan of the Proof
> Wu's outline at the end of the lecture. By Theorem [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-1|§28.1]], conditions (1)–(3) give $A \in \mathcal{L}(H, H)$ with $B(x, y) = (x, Ay)$. By the [[§27 Dual Spaces#^thm-27-2|Riesz representation theorem]], $\ell \in H'$ if and only if $\ell(x) = (x, a)$ for some $a \in H$. So the theorem says: for every $a \in H$ there is a unique $y$ with $Ay = a$. That is, *$A$ is one-to-one and onto*, and the coercivity (4) is what will be used to prove it. Wu said Lax–Milgram is “very useful in solving elliptic PDE”; examples are to come.

^rem-28-1

> [!remark] Remark: What is New in Lax–Milgram
> Wu's question: since the conclusion looks like the [[§27 Dual Spaces#^thm-27-2|Riesz representation theorem]], why is a new theorem needed? Compare $B$ with an inner product. Conditions (1)–(2) are the linearity of an inner product, (3) is the [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-1|Cauchy–Schwarz]] bound (with $M = 1$ for an inner product), and (4) is a quantitative form of $(x, x) = 0 \Rightarrow x = 0$. What is missing is the symmetry $B(x, y) = \overline{B(y, x)}$. When $B$ is symmetric there is nothing new: $B$ is itself an inner product (up to sign) and Lax–Milgram is the Riesz theorem for it. This is made precise below. What is new in Lax–Milgram is that it does not assume symmetry.

^rem-28-2

> [!remark]- Connections
> - Used in Electromagnetism: existence of the Dirichlet Green function of a bounded region — [[§C7.3 Green Functions for Poisson’s Equation#^rem-c7-3-1|EM ★ Remark: Existence of the Dirichlet Green function]].

![[m556-23-2.svg]]
*What is new in [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-2|Lax–Milgram]], for $B(x,y) = (x, Ay)$ on $\mathbb{R}^2$ with the non-symmetric $A$ shown, for which $\beta = 1$ and $M = \|A\| = 3$. (a) The curve $\{B(x,x) = 1\}$ (red) is the ellipse $2x_1^2 + x_2^2 = 1$ of the symmetric part $\tfrac12(A + A^{\mathsf T})$ — it cannot see the antisymmetric part of $A$ — and boundedness and coercivity trap it in the shaded annulus between the circles of radius $1/\sqrt{M}$ (dashed) and $1/\sqrt{\beta}$ (blue, the unit circle $(x,x) = 1$), which it touches at $\pm e_2$, where $B(x,x) = \beta\|x\|^2$. (b) The arrow $\tfrac14 Ax$ (red) drawn at each unit vector $x$ (blue dots). $A$ turns every $x$ clockwise, so it is not symmetric, but never by $90^\circ$ or more: $(x, Ax) = B(x,x) \ge \beta\|x\|^2 > 0$, so each arrow leaves the disc across the tangent line at $x$ (dashed at $x = e_2$, where the angle is $63^\circ$; the largest angle is about $65^\circ$). This is the property behind $A$ being one-to-one and onto ([[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^rem-28-1|plan of the proof]]). For a symmetric $B$ the red ellipse is the unit sphere of the inner product $\pm B$ and the Riesz theorem suffices ([[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^prop-28-4|§28.4]]). (Drawn for these notes in the vault; not in the course tex.)*

> [!theorem] Lemma §28.3: A Symmetric Coercive Form Has a Sign
> Let $B$ satisfy (1)–(4) of Theorem [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-2|§28.2]] and $B(x, y) = \overline{B(y, x)}$ for all $x, y$. Then either $B(x, x) \ge \beta\|x\|^2$ for all $x$, or $B(x, x) \le -\beta\|x\|^2$ for all $x$.

^lem-28-3

> [!proof]+ Proof
> (Not covered in lecture.) $B(x, x) = \overline{B(x, x)}$ is real, and by (4) it is nonzero for $x \neq 0$, with $|B(x,x)| \ge \beta\|x\|^2$. It suffices to show that $B(x, x)$ and $B(y, y)$ have the same sign for $x, y \neq 0$. If $y = cx$ with $c \in \mathbb{R}$, $c \neq 0$, then $B(y, y) = c^2 B(x, x)$. Otherwise $z(t) = (1 - t)x + ty \neq 0$ for every $t \in [0,1]$, and for real $t$
>
> $$
> f(t) = B(z(t), z(t)) = (1-t)^2 B(x,x) + t(1-t)\bigl( B(x,y) + B(y,x) \bigr) + t^2 B(y,y)
> $$
>
> is a real polynomial in $t$, never $0$ on $[0,1]$. By the [[§18 Properties of Continuous Functions#^thm-18-3|intermediate value theorem]] $f(0) = B(x,x)$ and $f(1) = B(y,y)$ have the same sign.

^pf-28-3

*Uses:* [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^def-28-1|Def. §28.1]], [[§18 Properties of Continuous Functions#^thm-18-3|451 §18.3]]

> [!theorem] Proposition §28.4: Symmetric Lax–Milgram is Riesz
> If $B$ satisfies (1)–(4) of Theorem [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-2|§28.2]] and $B(x, y) = \overline{B(y, x)}$ for all $x, y$, then the conclusion of Theorem [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-28-2|§28.2]] holds, and it follows from the [[§27 Dual Spaces#^thm-27-2|Riesz representation theorem]] applied to the inner product $((x, y)) = \pm B(x, y)$.
>
> *Lax: cf. §7.2, before (22)*

^prop-28-4

> [!proof]+ Proof
> (Wu's remark; the details are written out here.) By Lemma [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^lem-28-3|§28.3]], replacing $(B, \ell)$ by $(-B, -\ell)$ if necessary — which does not change the equation $\ell(x) = B(x, y)$ — we may assume $B(x, x) \ge \beta\|x\|^2$. Then $((x, y)) = B(x, y)$ is an inner product on $H$: it is linear in $x$ by (1), $((y, x)) = \overline{((x, y))}$ by symmetry, and $((x, x)) \ge \beta\|x\|^2 > 0$ for $x \neq 0$. Its norm $|||x||| = ((x,x))^{1/2}$ satisfies
>
> $$
> \beta\, \|x\|^2 \le |||x|||^2 \le M\, \|x\|^2 ,
> $$
>
> by coercivity and boundedness. So $|||\cdot|||$ and $\|\cdot\|$ are equivalent, they have the same Cauchy sequences and the same limits (Proposition [[§12 New Normed Spaces from Old#^prop-12-1|§12.1]]), and $(H, ((\cdot,\cdot)))$ is a Hilbert space. Given $\ell \in H'$, $|\ell(x)| \le \|\ell\|\,\|x\| \le \|\ell\|\, \beta^{-1/2}\, |||x|||$, so $\ell$ is bounded for the new norm as well. The [[§27 Dual Spaces#^thm-27-2|Riesz representation theorem]] in $(H, ((\cdot,\cdot)))$ gives a unique $y$ with $\ell(x) = ((x, y)) = B(x, y)$ for all $x$.

^pf-28-4

*Uses:* [[§28 Sesquilinear Forms and the Lax–Milgram Theorem#^lem-28-3|§28.3]], [[§20 Definition and Examples#^def-20-1|Def. §20.1]], [[§21 Cauchy–Schwarz and the Induced Norm#^thm-21-2|§21.2]], [[§12 New Normed Spaces from Old#^def-12-1|Def. §12.1]], [[§12 New Normed Spaces from Old#^prop-12-1|§12.1]], [[§21 Cauchy–Schwarz and the Induced Norm#^def-21-1|Def. §21.1]], [[§27 Dual Spaces#^def-27-1|Def. §27.1]], [[§27 Dual Spaces#^thm-27-2|§27.2]]
