---
type: section
subject: "[[Logic and Proofs]]"
chapter: 2
section: 9
eccles: "Ch. 9"
aliases: ["Eccles 9"]
tags: [logic-and-proofs, mat250]
---
← [[§8 Functions]] · ↑ [[· 2 Sets and Functions]] · [[§10 Counting]] →

*Eccles, Chapter 9 · MAT 250 HW4 (Exercises 9.1, 9.3–9.6) · MAT 200 lecture (syllabus week 9: Peano's axioms).*

A function assigns exactly one value to each point of its domain, but says nothing about how often each point of the codomain is hit. Asking for "at most once" gives injections, "at least once" surjections, and "exactly once" bijections; the bijections are precisely the functions that can be reversed. These notions are the basis of counting in [[§10 Counting|§10]]–[[§14 Counting Infinite Sets|§14]]. The section ends with images and preimages of subsets, and with Peano's axioms, which describe the positive integers by a single injective function.

## 9.1 Properties of Functions

> [!definition] Definition §9.1: Injection, Surjection, Bijection
> Let $f : X \to Y$ be a function.
> 1. $f$ is an **injection** (is **injective**, **one-to-one**) if no element of $Y$ is assigned to more than one element of $X$, i.e. $f$ takes different values at different points:
>
> $$
> \forall x_1, x_2 \in X,\ (x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)), \quad\text{equivalently (contrapositive)}\quad \forall x_1, x_2 \in X,\ (f(x_1) = f(x_2) \Rightarrow x_1 = x_2).
> $$
>
> 2. $f$ is a **surjection** (is **surjective**, **onto**) if each element of $Y$ is assigned to some element of $X$, i.e. each point of the codomain is a value:
>
> $$
> \forall y \in Y,\ \exists x \in X,\ y = f(x).
> $$
>
> 3. $f$ is a **bijection** (is **bijective**, **one-to-one and onto**) if it is both an injection and a surjection.
>
> *Eccles: Definition 9.1.1*

^def-9-1

> [!remark]- Connections
> - Same notions: [[§1 Countability and Set Theory#^def-1-3|551 Def. §1.3]], [[§1 Countability and Set Theory#^def-1-4|551 Def. §1.4]], [[§1 Countability and Set Theory#^def-1-6|551 Def. §1.6]].
> - For linear maps: [[§8 Null Spaces and Ranges#^ladr-3-14|LADR Def. 3.14]] (injective), [[§8 Null Spaces and Ranges#^ladr-3-19|LADR Def. 3.19]] (surjective).
> - Computational version: one-to-one functions and the horizontal line test, [[§5 Inverse Functions and Logarithms#^def-5-1|Calc Def. §5.1]] and [[§5 Inverse Functions and Logarithms#^thm-5-1|Calc Thm. §5.1]] (with worked examples).
> - For linear maps of ℝⁿ: [[§9 The Matrix of a Linear Transformation#^def-9-2|235 Def. §9.2]] (onto) and [[§9 The Matrix of a Linear Transformation#^def-9-3|235 Def. §9.3]] (one-to-one), tested by pivot positions in [[§9 The Matrix of a Linear Transformation#^thm-9-3|235 Thm. §9.3]], with worked examples.

> [!definition] Definition §9.2: Pre-image of an Element
> Let $f : X \to Y$ and $y \in Y$. A **pre-image** of $y$ (under $f$) is an element $x \in X$ such that $y = f(x)$.
>
> *Eccles: Definition 9.1.2*

^def-9-2

> [!theorem] Proposition §9.1: Injectivity and Surjectivity by Counting Pre-images
> Let $f : X \to Y$. Then
> 1. $f$ is injective $\iff$ every element of $Y$ has at most one pre-image;
> 2. $f$ is surjective $\iff$ every element of $Y$ has at least one pre-image;
> 3. $f$ is bijective $\iff$ every element of $Y$ has exactly one pre-image.
>
> *Eccles: Section 9.1 (after Definition 9.1.2)*

^prop-9-1

> [!proof]+ Proof
> (1) "$y$ has at most one pre-image" means: if $f(x_1) = y$ and $f(x_2) = y$ then $x_1 = x_2$. Requiring this for every $y \in Y$ is the same as requiring $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$ for all $x_1, x_2 \in X$ (take $y = f(x_1)$).
>
> (2) "$y$ has at least one pre-image" is $\exists x \in X,\ y = f(x)$; requiring it for every $y$ is the definition of surjectivity.
>
> (3) Combine (1) and (2): "exactly one" is "at least one and at most one".

^pf-9-1

*Uses:* [[§9 Injections, Surjections and Bijections#^def-9-1|Def. §9.1]], [[§9 Injections, Surjections and Bijections#^def-9-2|Def. §9.2]]

In each model of a function from [[§8 Functions|§8]]: in a **table of values**, $f$ is injective when no element occurs twice in the second row, surjective when every element of $Y$ occurs, and bijective when every element of $Y$ occurs exactly once. In the **arrow picture** we find pre-images by following arrows backwards; $f$ is bijective when every point of $Y$ is the end of exactly one arrow. In the **box model**, $f$ is injective when no two objects share a box, surjective when no box is empty, and bijective when every box holds exactly one object.

![[m250-9-1.svg]]
*Arrow pictures of the four possibilities. Injective: no point on the right receives two arrows. Surjective: every point on the right receives an arrow. Bijective: every point on the right receives exactly one arrow, so the arrows can be reversed to give a function back.*

> [!example] Example §9.1: The Functions of §8 Revisited
> **(a)** Of the eight functions $\{a, b, c\} \to \{d, e\}$ in [[§8 Functions#^ex-8-2|Example §8.2]](a), all except the constant functions $f_1$, $f_8$ are surjections, and none is an injection (three points, two values: two of $a, b, c$ share a value).
>
> **(b)** Of the four functions $\{a, b\} \to \{a, b\}$ in [[§8 Functions#^ex-8-2|Example §8.2]](b), the non-constant ones $g_2$ and $g_3$ are bijections. For any set $X$, the identity $I_X$ is a bijection.
>
> **(c)** For the four functions $x \mapsto x^2$ of [[§8 Functions#^ex-8-3|Example §8.3]]: $f_1 : \R \to \R$ is neither injective ($(-1)^2 = 1^2$) nor surjective (no real $x$ has $x^2 = -1$); $f_2 : \R^{\geq} \to \R$ is injective (for $0 \le x_1 < x_2$, $x_1^2 < x_2^2$) but not surjective; $f_3 : \R \to \R^{\geq}$ is surjective (each $y \ge 0$ is $(\sqrt{y})^2$) but not injective; $f_4 : \R^{\geq} \to \R^{\geq}$ is a bijection. A result proved for injections applies to $f_2$ and $f_4$ but not to $f_1$ and $f_3$: domain and codomain matter.
>
> *Eccles: Examples 9.1.3 (in (b) Eccles writes $f_2$, $f_3$ for $g_2$, $g_3$)*

^ex-9-1

> [!remark] Remark: Every Function Becomes a Surjection
> Changing the codomain to the image makes any function surjective: for $f : X \to Y$, the same assignment defines $f^+ : X \to \operatorname{Im} f$, $f^+(x) = f(x)$, and every element of $\operatorname{Im} f$ is by definition $f(x) = f^+(x)$ for some $x$. Injectivity cannot be repaired this way; it needs a smaller domain (see [[§9 Injections, Surjections and Bijections#^ex-9-6|Example §9.6]]).
>
> *Eccles: Remarks 9.1.4*

^rem-9-1

Since injectivity and surjectivity are universal and existential statements, they are proved and disproved by the methods of [[§7 Quantifiers|§7]]: a single pair $x_1 \ne x_2$ with $f(x_1) = f(x_2)$ disproves injectivity, and a single $y$ with no pre-image disproves surjectivity. Often the most efficient method is to **solve $y = f(x)$ for $x$**, which finds all pre-images of a general $y$ at once.

> [!example] Example §9.2: The Same Formula on Different Sets
> **(a)** $f_1 : \R \to \R$, $f_1(x) = x + 1$. For $x, y \in \R$,
>
> $$
> x \text{ is a pre-image of } y \iff y = x + 1 \iff x = y - 1 ,
> $$
>
> so each $y \in \R$ has exactly one pre-image, $y - 1$, and $f_1$ is a bijection ([[§9 Injections, Surjections and Bijections#^prop-9-1|Proposition §9.1]]).
>
> **(b)** $f_2 : \R^+ \to \R^+$, $f_2(x) = x + 1$. The same computation gives the only candidate $x = y - 1$, but a pre-image must lie in the domain $\R^+$, and $y - 1 \in \R^+ \iff y > 1$. So $\operatorname{Im} f_2 = \{y \in \R^+ \mid y > 1\} \ne \R^+$.
>
> *Solution:* $f_2$ is injective, since for $x_1, x_2 \in \R^+$, $f_2(x_1) = f_2(x_2) \Rightarrow x_1 + 1 = x_2 + 1 \Rightarrow x_1 = x_2$. It is not surjective: for $x \in \R^+$, $f_2(x) = x + 1 > 1$, so $\frac12 \in \R^+$ is not a value.
>
> *Eccles: Examples 9.1.5, 9.1.6*

^ex-9-2

> [!example] Example §9.3: A Quadratic on Different Sets
> **(a)** $f_3 : \R \to \R$, $f_3(x) = 4x^2 - 4x + 2$. Solving,
>
> $$
> y = f_3(x) \iff y = (2x - 1)^2 + 1 \iff x = \frac{1 \pm \sqrt{y - 1}}{2}.
> $$
>
> The formula makes sense only for $y \ge 1$, and the $\pm$ gives two pre-images whenever $y > 1$. *Solution:* $f_3(0) = f_3(1) = 2$, so $f_3$ is not injective; $f_3(x) = (2x - 1)^2 + 1 \ge 1$ for all $x$, so $0$ is not a value and $f_3$ is not surjective.
>
> **(b)** $f_4 : \R^+ \to \{y \in \R^+ \mid y \ge 1\}$, the same formula. Now every $y$ in the codomain has $y \ge 1$, and $x = \frac{1 + \sqrt{y - 1}}{2} \ge \frac12 > 0$ is a pre-image in $\R^+$, so $f_4$ is surjective. The second candidate $\frac{1 - \sqrt{y - 1}}{2}$ lies in $\R^+$ exactly when $\sqrt{y - 1} < 1$, i.e. $y < 2$, so values $1 < y < 2$ have two pre-images. *Solution:* $f_4$ is surjective as shown, and not injective since $f_4(\frac14) = f_4(\frac34) = \frac54$ (from $y = \frac54$, $\sqrt{y - 1} = \frac12$).
>
> A formal proof need not say how a counterexample was found, but it helps the reader to show it (here: from the completed square, or a sketch of the graph).
>
> *Eccles: Examples 9.1.7, 9.1.8*

^ex-9-3

> [!example] Example §9.4: Four Functions on the Reals
> Which of these functions $\R \to \R$ are injective, surjective, bijective?
>
> **(i)** $f_1(x) = 2x + 5$. Since $y = 2x + 5 \iff x = (y - 5)/2$ for $x, y \in \R$, each $y$ has exactly one pre-image: $f_1$ is a **bijection**.
>
> **(ii)** $f_2(x) = x^2 + 2x + 1 = (x + 1)^2$. Not injective: $f_2(0) = f_2(-2) = 1$. Not surjective: $(x + 1)^2 \ge 0$, so $-1$ is not a value. (Solving, $y = (x + 1)^2 \iff x = -1 \pm \sqrt{y}$, which needs $y \ge 0$.)
>
> **(iii)** $f_3(x) = x^2 - 2x = (x - 1)^2 - 1$. Not injective: $f_3(0) = f_3(2) = 0$. Solving, $y = f_3(x) \iff (x - 1)^2 = y + 1 \iff x = 1 \pm \sqrt{y + 1}$, so $y$ has a pre-image exactly when $y \ge -1$: $\operatorname{Im} f_3 = [-1, \infty)$. Not surjective: $-2$ is not a value, since $f_3(x) \ge -1$ for all $x$.
>
> **(iv)** $f_4(x) = 1/x$ for $x \ne 0$, $f_4(0) = 0$. For $x \ne 0$, $f_4(x) = 1/x \ne 0$ and $f_4(1/x) = x$; also $f_4(f_4(0)) = 0$. So $f_4 \circ f_4 = I_\R$, and $f_4$ is its own inverse; by [[§9 Injections, Surjections and Bijections#^prop-9-3|Proposition §9.3]] and [[§9 Injections, Surjections and Bijections#^thm-9-2|Theorem §9.2]] it is a **bijection**. (Directly: $y \ne 0$ has the single pre-image $1/y$, and $0$ the single pre-image $0$.)
>
> *Source: HW4*
> *Eccles: Exercise 9.1*
>
> *The HW4 solution to (iii) says that every $y < 0$ has no pre-image; in fact $y$ has one exactly when $y \ge -1$ (e.g. $f_3(1 - 1/\sqrt{2}) = -\tfrac12$), so the missing value has to be some $y < -1$, such as $-2$.*

^ex-9-4

## 9.2 Bijections and Inverses

> [!definition] Definition §9.3: Invertible Function; Inverse
> A function $f : X \to Y$ is **invertible** if there exists a function $g : Y \to X$ such that
>
> $$
> y = f(x) \iff x = g(y) \qquad \text{for all } x \in X \text{ and all } y \in Y .
> $$
>
> Such a $g$ is an **inverse** (function) of $f$, written $g = f^{-1}$. The condition is symmetric in $f$ and $g$, so then $g$ is also invertible and $f$ is an inverse of $g$. (The "if" in this definition means "if and only if", as in every definition.)
>
> *Eccles: Definition 9.2.1*

^def-9-3

> [!remark]- Connections
> - Computational version: [[§5 Inverse Functions and Logarithms#^def-5-2|Calc Def. §5.2]] (with worked examples).
> - For linear maps of ℝⁿ: [[§13 Characterizations of Invertible Matrices#^def-13-1|235 Def. §13.1]] (invertible linear transformation).

> [!example] Example §9.5: A Pair of Inverse Functions
> $f : \R \to \R$, $f(x) = 2x + 1$, and $g : \R \to \R$, $g(x) = (x - 1)/2$, are inverse to each other: for $x, y \in \R$,
>
> $$
> y = f(x) \iff y = 2x + 1 \iff x = (y - 1)/2 \iff x = g(y).
> $$
>
> *Eccles: Example 9.2.2*

^ex-9-5

> [!theorem] Theorem §9.2: Invertible Means Bijective
> Let $f : X \to Y$. Then $f$ is invertible if and only if it is a bijection. Furthermore, if $f$ is invertible then its inverse is unique.
>
> *Eccles: Theorem 9.2.3*

^thm-9-2

> [!proof]+ Proof
> *Idea.* In the box model, a bijection puts exactly one object in each box, and the inverse sends each box to the object it contains; this is possible only if each box holds exactly one object. The proof spells out the definitions; at each step there is essentially one way forward. The uniqueness claim is proved in the standard way: assume two inverses $g_1$, $g_2$ and show $g_1 = g_2$.
>
> **(a) Invertible $\Rightarrow$ bijective.** Let $g : Y \to X$ be an inverse of $f$, so $y = f(x) \iff x = g(y)$ for all $x \in X$, $y \in Y$.
>
> *Injective:* let $x_1, x_2 \in X$ with $f(x_1) = f(x_2)$, and put $y_0 = f(x_1) = f(x_2)$. From $y_0 = f(x_1)$ we get $x_1 = g(y_0)$, and from $y_0 = f(x_2)$ we get $x_2 = g(y_0)$. Hence $x_1 = g(y_0) = x_2$.
>
> *Surjective:* let $y_0 \in Y$ and put $x_0 = g(y_0)$. Then $x_0 = g(y_0)$ gives $y_0 = f(x_0)$.
>
> **(b) Bijective $\Rightarrow$ invertible.** Let $f$ be a bijection. By [[§9 Injections, Surjections and Bijections#^prop-9-1|Proposition §9.1]](3), each $y \in Y$ has exactly one pre-image; define $g(y)$ to be that unique $x \in X$ with $f(x) = y$. This assigns a unique element of $X$ to each $y \in Y$, so $g : Y \to X$ is a function, and by construction $x = g(y) \iff f(x) = y$. So $g$ is an inverse of $f$.
>
> **(c) Uniqueness.** Let $g_1, g_2 : Y \to X$ both be inverses of $f$. Let $y_0 \in Y$, and put $x_1 = g_1(y_0)$, $x_2 = g_2(y_0)$. Then $x_1 = g_1(y_0)$ gives $y_0 = f(x_1)$, and $x_2 = g_2(y_0)$ gives $y_0 = f(x_2)$. So $f(x_1) = f(x_2)$; since $f$ is invertible it is injective by (a), and $x_1 = x_2$. Thus $g_1(y_0) = g_2(y_0)$ for every $y_0 \in Y$, i.e. $g_1 = g_2$.

^pf-9-2

*Uses:* [[§9 Injections, Surjections and Bijections#^def-9-3|Def. §9.3]], [[§9 Injections, Surjections and Bijections#^def-9-1|Def. §9.1]], [[§9 Injections, Surjections and Bijections#^prop-9-1|§9.1]], [[§8 Functions#^def-8-3|Def. §8.3]]

> [!remark]- Connections
> - Same result stated with $g \circ f$ and $f \circ g$: [[§21 Algebra Prerequisites꞉ Groups#^prop-21-4|590 Prop. §21.4]].
> - For linear maps: [[§10 Invertibility and Isomorphisms#^ladr-3-63|LADR Thm. 3.63]] (invertible iff injective and surjective), with uniqueness of the inverse in [[§10 Invertibility and Isomorphisms#^ladr-3-60|LADR Thm. 3.60]].
> - In Stewart the inverse is defined exactly for one-to-one functions onto their range: [[§5 Inverse Functions and Logarithms#^def-5-2|Calc Def. §5.2]].
> - For linear maps of ℝⁿ: [[§13 Characterizations of Invertible Matrices#^rem-13-2|235 Remark §13.2]] (invertible means one-to-one and onto, read off from pivots) and [[§13 Characterizations of Invertible Matrices#^thm-13-3|235 Thm. §13.3]] (T is invertible iff its matrix is).

Because of Theorem §9.2, "bijective" and "invertible" are used interchangeably. Many standard functions are not bijections, but become bijections after restricting the domain and shrinking the codomain.

> [!example] Example §9.6: Inverse Functions From Calculus
> Using facts from calculus (not proved here):
>
> **(a)** $\sin : \R \to \R$ is not injective ($\sin 0 = \sin \pi$) and not surjective (no $x$ has $\sin x = 2$). Its image is $[-1, 1]$, and on $[-\pi/2, \pi/2]$ it increases steadily from $-1$ to $1$, so $\sin : [-\pi/2, \pi/2] \to [-1, 1]$ is a bijection (still called $\sin$, by the usual abuse). Its inverse is $\sin^{-1} : [-1, 1] \to [-\pi/2, \pi/2]$. Another choice of interval, such as $[\pi/2, 3\pi/2]$, gives another inverse; the choice made is the **principal value**. Likewise $\cos^{-1} : [-1, 1] \to [0, \pi]$ and $\tan^{-1} : \R \to (-\pi/2, \pi/2)$.
>
> **(b)** For $n \in \Z^+$ odd, $x \mapsto x^n$ is a bijection $\R \to \R$; its inverse is the **$n$th root**, $x \mapsto x^{1/n} = \sqrt[n]{x}$. For $n$ even, $x \mapsto x^n$ is neither injective nor surjective on $\R$ (the case $n = 2$ is [[§9 Injections, Surjections and Bijections#^ex-9-1|Example §9.1]](c)), but it is a bijection $\R^{\geq} \to \R^{\geq}$, whose inverse $\R^{\geq} \to \R^{\geq}$ gives the non-negative $n$th root.
>
> *Eccles: Examples 9.2.4*

^ex-9-6

> [!theorem] Proposition §9.3: Inverses via Composition
> Functions $f : X \to Y$ and $g : Y \to X$ are inverses of each other if and only if
>
> $$
> g \circ f = I_X \quad\text{and}\quad f \circ g = I_Y .
> $$
>
> *Eccles: Proposition 9.2.5*

^prop-9-3

> [!proof]+ Proof
> "$\Rightarrow$": suppose $y = f(x) \iff x = g(y)$ for all $x \in X$, $y \in Y$. Given $x_0 \in X$, put $y_0 = f(x_0)$; then $x_0 = g(y_0)$, so $(g \circ f)(x_0) = g(y_0) = x_0$. Hence $g \circ f = I_X$. Similarly, given $y_0 \in Y$, put $x_0 = g(y_0)$; then $y_0 = f(x_0)$, so $(f \circ g)(y_0) = y_0$, and $f \circ g = I_Y$.
>
> "$\Leftarrow$": suppose $g \circ f = I_X$ and $f \circ g = I_Y$. If $y = f(x)$, then $g(y) = g(f(x)) = I_X(x) = x$. If $x = g(y)$, then $f(x) = f(g(y)) = I_Y(y) = y$. So $y = f(x) \iff x = g(y)$ for all $x \in X$, $y \in Y$.

^pf-9-3

*Uses:* [[§9 Injections, Surjections and Bijections#^def-9-3|Def. §9.3]], [[§8 Functions#^def-8-5|Def. §8.5]], [[§8 Functions#^def-8-2|Def. §8.2]], [[§8 Functions#^def-8-3|Def. §8.3]]

> [!remark]- Connections
> - Computational version: the cancellation equations, [[§5 Inverse Functions and Logarithms#^thm-5-2|Calc Thm. §5.2]].

> [!example] Example §9.7: Finding Inverses
> **(i)** $f_1 : \R \to \R$, $f_1(x) = 3x + 2$. For $x, y \in \R$: $y = 3x + 2 \iff x = (y - 2)/3$. So $f_1^{-1}(y) = (y - 2)/3$.
>
> **(ii)** $f_2 : \R \to \R$, $f_2(x) = x^3 + 1$. For $x, y \in \R$: $y = x^3 + 1 \iff x^3 = y - 1 \iff x = \sqrt[3]{y - 1}$, the last step because cubing is a bijection $\R \to \R$ with inverse the real cube root ([[§9 Injections, Surjections and Bijections#^ex-9-6|Example §9.6]](b)). So $f_2^{-1}(y) = \sqrt[3]{y - 1}$.
>
> In both cases the chain of equivalences is exactly the condition of [[§9 Injections, Surjections and Bijections#^def-9-3|Def. §9.3]], so it proves at once that $f_i$ is invertible (hence bijective) and identifies the inverse.
>
> *Source: HW4*
> *Eccles: Exercise 9.3*

^ex-9-7

> [!example] Example §9.8: Composites of Injections and of Surjections
> Let $f : X \to Y$ and $g : Y \to Z$.
>
> **(a)** If $f$ and $g$ are injections, so is $g \circ f$. Let $x_1, x_2 \in X$ with $(g \circ f)(x_1) = (g \circ f)(x_2)$, i.e. $g(f(x_1)) = g(f(x_2))$. Since $g$ is injective, $f(x_1) = f(x_2)$; since $f$ is injective, $x_1 = x_2$.
>
> **(b)** If $f$ and $g$ are surjections, so is $g \circ f$. Let $z \in Z$. Since $g$ is surjective there is $y \in Y$ with $g(y) = z$, and since $f$ is surjective there is $x \in X$ with $f(x) = y$. Then $(g \circ f)(x) = g(y) = z$.
>
> **(c)** Hence a composite of bijections is a bijection; [[§9 Injections, Surjections and Bijections#^ex-9-9|Example §9.9]] also identifies its inverse.
>
> *Source: HW4 (part (a))*
> *Eccles: Exercise 9.4; Problems II, Question 18*

^ex-9-8

> [!example] Example §9.9: The Inverse of a Composite
> **Claim:** if $f : X \to Y$ and $g : Y \to Z$ are bijections, then $g \circ f : X \to Z$ is a bijection and
>
> $$
> (g \circ f)^{-1} = f^{-1} \circ g^{-1} : Z \to Y \to X .
> $$
>
> By [[§9 Injections, Surjections and Bijections#^thm-9-2|Theorem §9.2]], $f^{-1} : Y \to X$ and $g^{-1} : Z \to Y$ exist. For $x \in X$ and $z \in Z$,
>
> $$
> z = (g \circ f)(x) \iff z = g(f(x)) \iff g^{-1}(z) = f(x) \iff f^{-1}(g^{-1}(z)) = x \iff x = (f^{-1} \circ g^{-1})(z),
> $$
>
> using the defining property of $g^{-1}$ (with $f(x) \in Y$) and then of $f^{-1}$. So $f^{-1} \circ g^{-1}$ is an inverse of $g \circ f$ ([[§9 Injections, Surjections and Bijections#^def-9-3|Def. §9.3]]); hence $g \circ f$ is invertible, so bijective, and since the inverse is unique it equals $f^{-1} \circ g^{-1}$.
>
> Alternatively, by [[§9 Injections, Surjections and Bijections#^prop-9-3|Proposition §9.3]] and associativity ([[§8 Functions#^prop-8-1|Proposition §8.1]]): $(f^{-1} \circ g^{-1}) \circ (g \circ f) = f^{-1} \circ (g^{-1} \circ g) \circ f = f^{-1} \circ I_Y \circ f = f^{-1} \circ f = I_X$, and similarly $(g \circ f) \circ (f^{-1} \circ g^{-1}) = I_Z$. Note the reversal of order, as when taking off shoes and socks.
>
> *Source: HW4*
> *Eccles: Exercise 9.5*

^ex-9-9

> [!remark]- Connections
> - The bijections $X \to X$ are closed under composition and inverses, and form the symmetric group [[§3 Basic Examples of Groups#^def-3-5|493 Def. §3.5]].

## 9.3 Functions and Subsets

The notation $f^{-1}$ is also used when $f$ is not a bijection, for a function between power sets. A function $f : X \to Y$ gives two functions between $\mathcal{P}(X)$ and $\mathcal{P}(Y)$ ([[§6 The Language of Set Theory#^def-6-9|Def. §6.9]]), one in each direction.

> [!definition] Definition §9.4: Image and Pre-image of a Subset
> Let $f : X \to Y$ be a function.
> 1. $\overrightarrow{f} : \mathcal{P}(X) \to \mathcal{P}(Y)$ is defined by $\overrightarrow{f}(A) = \{f(x) \mid x \in A\}$ for $A \subseteq X$, the **image** of $A$.
> 2. $\overleftarrow{f} : \mathcal{P}(Y) \to \mathcal{P}(X)$ is defined by $\overleftarrow{f}(B) = \{x \in X \mid f(x) \in B\}$ for $B \subseteq Y$, the **pre-image** (or inverse image) of $B$.
>
> *Eccles: Definition 9.3.1*

^def-9-4

> [!remark] Remark: Notation, and the Two Extensions
> Most writers denote $\overrightarrow{f}(A)$ simply by $f(A)$ and $\overleftarrow{f}(B)$ by $f^{-1}(B)$ (as in Topology and Measure Theory); Eccles's arrows avoid giving two different functions the same name. $\overrightarrow{f}$ extends $f$: $\overrightarrow{f}(\{x_0\}) = \{f(x_0)\}$, and $\overrightarrow{f}(X) = \operatorname{Im} f$. $\overleftarrow{f}(\{y_0\}) = \{x \in X \mid f(x) = y_0\}$ is the set of pre-images of $y_0$, the contents of box $y_0$. If $f$ is a bijection, $\overleftarrow{f}(\{y_0\}) = \{f^{-1}(y_0)\}$, so $\overleftarrow{f}$ extends $f^{-1}$; if $f$ is not surjective, $\overleftarrow{f}(\{y\}) = \emptyset$ for $y \notin \operatorname{Im} f$, and if $f$ is not injective, $\overleftarrow{f}(\{y\})$ has more than one element for some $y$.
>
> *Eccles: Remarks 9.3.2*

^rem-9-2

> [!example] Example §9.10: Pre-images Respect Inclusion, Intersection and Union
> Let $f : X \to Y$ and $B_1, B_2 \subseteq Y$. Then
> 1. $B_1 \subseteq B_2 \Rightarrow \overleftarrow{f}(B_1) \subseteq \overleftarrow{f}(B_2)$;
> 2. $\overleftarrow{f}(B_1 \cap B_2) = \overleftarrow{f}(B_1) \cap \overleftarrow{f}(B_2)$;
> 3. $\overleftarrow{f}(B_1 \cup B_2) = \overleftarrow{f}(B_1) \cup \overleftarrow{f}(B_2)$.
>
> (1) If $B_1 \subseteq B_2$, then $x \in \overleftarrow{f}(B_1) \Rightarrow f(x) \in B_1 \Rightarrow f(x) \in B_2 \Rightarrow x \in \overleftarrow{f}(B_2)$.
>
> (2) $x \in \overleftarrow{f}(B_1 \cap B_2) \iff f(x) \in B_1$ and $f(x) \in B_2 \iff x \in \overleftarrow{f}(B_1) \cap \overleftarrow{f}(B_2)$.
>
> (3) The same with "or" in place of "and".
>
> The converse of (1) is false: for $f : \{a\} \to \{a, b\}$, $f(a) = a$, and $B_1 = \{b\}$, $B_2 = \{a\}$, we have $\overleftarrow{f}(B_1) = \emptyset \subseteq \{a\} = \overleftarrow{f}(B_2)$ but $B_1 \not\subseteq B_2$. The trouble is the element $b$, which is not a value. The converse does hold when $f$ is surjective: if $y \in B_1$, write $y = f(x)$; then $x \in \overleftarrow{f}(B_1) \subseteq \overleftarrow{f}(B_2)$, so $y = f(x) \in B_2$.
>
> *Eccles: Exercise 9.7*

^ex-9-10

> [!example] Example §9.11: Surjectivity From the Graph
> **Claim:** $f : X \to Y$ is surjective if and only if every horizontal line meets the graph: $\forall y \in Y,\ (X \times \{y\}) \cap G_f \ne \emptyset$.
>
> For fixed $y \in Y$, an element of $(X \times \{y\}) \cap G_f$ is a pair $(x, y)$ with $x \in X$ and $y = f(x)$ ([[§8 Functions#^def-8-10|Def. §8.10]]), so
>
> $$
> (X \times \{y\}) \cap G_f = \{(x, y) \mid x \in X,\ f(x) = y\},
> $$
>
> which is non-empty if and only if $\exists x \in X,\ f(x) = y$, i.e. $y$ has a pre-image. Requiring this for all $y \in Y$ is surjectivity. (Compare [[§8 Functions#^prop-8-2|Proposition §8.2]]: every *vertical* line meets a graph exactly once; $f$ is surjective when every *horizontal* line meets it at least once, and by [[§9 Injections, Surjections and Bijections#^prop-9-1|Proposition §9.1]] injective when every horizontal line meets it at most once.)
>
> *Source: HW4*
> *Eccles: Exercise 9.6*
>
> *The HW4 solution replaces $X \times \{y\}$ by $X \times Y$ in the middle step, which turns the intersection into all of $G_f$; the intersection has to be computed with the line $X \times \{y\}$ itself, as above.*

^ex-9-11

> [!remark]- Connections
> - The analogous test for injectivity: the horizontal line test, [[§5 Inverse Functions and Logarithms#^thm-5-1|Calc Thm. §5.1]].

## 9.4 Peano's Axioms for the Natural Numbers

The successor of an integer was used to explain the induction principle ([[§5 The Induction Principle#^rem-5-1|§5, remark after Def. §5.1]]); Dedekind observed that the successor function together with the number $1$ captures everything about the positive integers.

> [!definition] Definition §9.5: Successor Function
> The **successor function** $s : \Z^+ \to \Z^+$ is defined by $s(n) = n + 1$ for $n \in \Z^+$.
>
> *Eccles: Definition 9.4.1*

^def-9-5

> [!definition] Definition §9.6: Peano's Axioms
> The set of positive integers $\Z^+$ is a set with a function $s : \Z^+ \to \Z^+$ and an element $1 \in \Z^+$ such that
> 1. $s$ is an injection;
> 2. $1$ is not in the image of $s$;
> 3. for $A \subseteq \Z^+$, if $1 \in A$ and $n \in A \Rightarrow s(n) \in A$, then $A = \Z^+$.
>
> *Eccles: Axioms 9.4.2*
> *Source: MAT 200 lecture (syllabus week 9)*

^def-9-6

> [!remark] Remark: What the Axioms Say
> Axiom 3 is the induction principle ([[§5 The Induction Principle#^def-5-1|Def. §5.1]]) in the set form of [[§7 Quantifiers#^def-7-4|Def. §7.4]]. Axiom 1 says distinct numbers have distinct successors, and axiom 2 that counting has a starting point; together with 3 they say that $1, s(1), s(s(1)), \ldots$ runs through $\Z^+$ without repetition. These are axioms *for* $\Z^+$ in the sense that any set $X$ with a function $s : X \to X$ and an element $1 \in X$ satisfying them is in bijection with $\Z^+$ by a bijection matching the two elements $1$ and the two successor functions (Dedekind; proved by induction, not proved here). Addition and multiplication can then be *defined* from $s$.
>
> *Eccles: Section 9.4*

^rem-9-3

> [!remark]- Connections
> - Developed further in: [[§1 The Set ℕ of Natural Numbers#^def-1-1|451 Def. §1.1]] (Peano axioms for $\N = \{1, 2, \ldots\}$, the same three axioms with "$s$ is a function into $\N$" split off), from which 451 derives induction in [[§1 The Set ℕ of Natural Numbers#^thm-1-1|451 Thm. §1.1]].

> [!definition] Definition §9.7: Addition and Multiplication From the Successor
> The **sum** $m + n$ of positive integers is defined by induction on $n$:
> 1. $m + 1 = s(m)$;
> 2. $m + s(k) = s(m + k)$ for $k \in \Z^+$.
>
> The **product** $m \times n$ is then defined by induction on $n$:
> 1. $m \times 1 = m$;
> 2. $m \times s(k) = m \times k + m$ for $k \in \Z^+$.
>
> *Eccles: Definition 9.4.3 (printed "$m \times (k)$" in (2); it is $m \times s(k)$)*

^def-9-7

> [!example] Example §9.12: Every Positive Integer Other Than 1 Is a Successor
> **Claim:** if $n \in \Z^+$ and $n \ne 1$, then $n = s(a)$ for some $a \in \Z^+$.
>
> Let $A = \operatorname{Im}(s) \cup \{1\} \subseteq \Z^+$. Then $1 \in A$; and if $n \in A$ then $s(n) \in \operatorname{Im}(s) \subseteq A$. By [[§9 Injections, Surjections and Bijections#^def-9-6|Def. §9.6]](3), $A = \Z^+$. So every $n \ne 1$ lies in $\operatorname{Im}(s)$. (By axiom 1 this $a$ is unique, and by axiom 2 the number $1$ itself is not a successor: every positive integer except $1$ has exactly one predecessor.)
>
> *Eccles: Problems II, Question 22*

^ex-9-12

> [!example] Example §9.13: Addition Is Associative and Commutative
> From [[§9 Injections, Surjections and Bijections#^def-9-7|Def. §9.7]] and [[§9 Injections, Surjections and Bijections#^def-9-6|Def. §9.6]](3), used as proof by induction ([[§5 The Induction Principle#^def-5-1|Def. §5.1]]):
>
> **(i) Associativity:** $(a + b) + c = a + (b + c)$ for all $a, b, c \in \Z^+$. Fix $a, b$ and induct on $c$. For $c = 1$: $(a + b) + 1 = s(a + b) = a + s(b) = a + (b + 1)$. If it holds for $c = k$, then
>
> $$
> (a + b) + s(k) = s\big((a + b) + k\big) = s\big(a + (b + k)\big) = a + s(b + k) = a + \big(b + s(k)\big),
> $$
>
> using Def. §9.7(2) three times and the inductive hypothesis once. So it holds for $c = s(k)$.
>
> **(ii) Commutativity:** $a + b = b + a$. *Step 1:* $a + 1 = 1 + a$, by induction on $a$. For $a = 1$ it is trivial. If $k + 1 = 1 + k$, then $s(k) + 1 = s(s(k))$ and $1 + s(k) = s(1 + k) = s(k + 1) = s(s(k))$, so $s(k) + 1 = 1 + s(k)$.
>
> *Step 2:* fix $a$ and induct on $b$. For $b = 1$ this is Step 1. If $a + k = k + a$, then
>
> $$
> a + s(k) = s(a + k) = s(k + a), \qquad s(k) + a = (k + 1) + a = k + (1 + a) = k + (a + 1) = (k + a) + 1 = s(k + a),
> $$
>
> using (i) twice and Step 1. So $a + s(k) = s(k) + a$.
>
> *Eccles: Problems II, Question 23*

^ex-9-13
