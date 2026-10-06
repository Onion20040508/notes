---
type: section
subject: "[[Logic and Proofs]]"
chapter: 2
section: 8
eccles: "Ch. 8"
aliases: ["Eccles 8"]
tags: [logic-and-proofs, mat250]
---
← [[§7 Quantifiers]] · ↑ [[· 2 Sets and Functions]] · [[§9 Injections, Surjections and Bijections]] →

*Eccles, Chapter 8 · MAT 250 HW3 (Exercises 8.2, 8.4, 8.5).*

A function is an assignment of a unique element of $Y$ to each element of $X$; the domain and codomain are part of the function, and a function is determined by its values, not by the formula used to compute them. This section introduces functions and the basic ways of making new ones (restriction, composition), sequences and the first limit definition (a null sequence, three quantifiers deep), the image, and the graph, which turns a function into a subset of $X \times Y$.

## 8.1 Functions and Formulae

> [!definition] Definition §8.1: Function
> Let $X$ and $Y$ be sets. A **function** (or **map**, or **mapping**) $f$ from $X$ to $Y$, written $f : X \to Y$, is the assignment of a unique element of $Y$ to each element of $X$. The element assigned to $x \in X$ is denoted $f(x)$, and we write $x \mapsto f(x)$. The element $f(x) \in Y$ is the **value** of $f$ at $x$, or the **image** of $x$ under $f$. The set $X$ is the **domain** of $f$ and $Y$ is its **codomain**.
>
> *Eccles: Definition 8.1.1*

^def-8-1

> [!remark]- Connections
> - Same notion: [[§1 Countability and Set Theory#^def-1-2|551 Def. §1.2]] (mapping).
> - Stewart's definition: [[§1 Four Ways to Represent a Function#^def-1-1|Calc Def. §1.1]].
> - Computational version: [[§8 Introduction to Linear Transformations#^def-8-1|235 Def. §8.1]] (transformations from ℝⁿ to ℝᵐ, with domain, codomain, image and range).

> [!example] Example §8.1: Three Pictures of One Function
> Let $X = \{x_1, x_2, x_3, x_4\}$ and $Y = \{y_1, y_2, y_3, y_4, y_5\}$. The table
>
> | $x$ | $x_1$ | $x_2$ | $x_3$ | $x_4$ |
> |:-:|:-:|:-:|:-:|:-:|
> | $f(x)$ | $y_1$ | $y_1$ | $y_3$ | $y_5$ |
>
> determines a function $f : X \to Y$: each element of the domain occurs exactly once in the first row, so reading down gives a well-defined value. An element of the codomain may occur once, several times, or not at all in the second row.
>
> The same function can be drawn with arrows (figure below): exactly one arrow starts at each element of $X$, while an element of $Y$ may be the end of one arrow, several, or none. Or think of the elements of $Y$ as boxes and of $f$ as a way of placing the elements of $X$ into the boxes: here box $y_1$ holds $x_1, x_2$, box $y_3$ holds $x_3$, box $y_5$ holds $x_4$, and boxes $y_2, y_4$ are empty. Each element of $X$ goes into exactly one box.
>
> *Eccles: Example 8.1.2*

^ex-8-1

![[m250-8-1.svg]]
*The arrow picture of the function in [[§8 Functions#^ex-8-1|Example §8.1]]. The defining property of a function is on the left: one arrow leaves each element of the domain. On the right anything is allowed: $y_1$ receives two arrows, $y_2$ and $y_4$ none.*

> [!definition] Definition §8.2: Constant Function
> Given sets $X$, $Y$ and $y_0 \in Y$, the **constant function** $c_{y_0} : X \to Y$ is given by $c_{y_0}(x) = y_0$ for all $x \in X$.
>
> *Eccles: Examples 8.1.3, 8.1.4*

^def-8-2

> [!definition] Definition §8.2: Identity Function
> Given a set $X$, the **identity function** $I_X : X \to X$ is given by $I_X(x) = x$ for all $x \in X$.
>
> *Eccles: Examples 8.1.3, 8.1.4*

^def-8-new1

> [!example] Example §8.2: All Functions Between Small Sets
> **(a)** For $X = \{a, b, c\}$ and $Y = \{d, e\}$ there are exactly eight functions $X \to Y$, one for each way of choosing a value in $\{d, e\}$ at each of $a, b, c$:
>
> | $x$ | $f_1$ | $f_2$ | $f_3$ | $f_4$ | $f_5$ | $f_6$ | $f_7$ | $f_8$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | $a$ | $d$ | $d$ | $d$ | $d$ | $e$ | $e$ | $e$ | $e$ |
> | $b$ | $d$ | $d$ | $e$ | $e$ | $d$ | $d$ | $e$ | $e$ |
> | $c$ | $d$ | $e$ | $d$ | $e$ | $d$ | $e$ | $d$ | $e$ |
>
> $f_1 = c_d$ and $f_8 = c_e$ are the constant functions.
>
> **(b)** For $Z = \{a, b\}$ there are exactly four functions $Z \to Z$:
>
> | $x$ | $g_1$ | $g_2$ | $g_3$ | $g_4$ |
> |:-:|:-:|:-:|:-:|:-:|
> | $a$ | $a$ | $a$ | $b$ | $b$ |
> | $b$ | $a$ | $b$ | $a$ | $b$ |
>
> $g_1$ and $g_4$ are constant, and $g_2 = I_Z$ is the identity.
>
> *Eccles: Examples 8.1.3, 8.1.4*

^ex-8-2

> [!example] Example §8.3: One Formula, Four Functions
> The formula $x \mapsto x^2$ gives four different functions:
>
> $$
> f_1 : \R \to \R, \qquad f_2 : \R^{\geq} \to \R, \qquad f_3 : \R \to \R^{\geq}, \qquad f_4 : \R^{\geq} \to \R^{\geq}, \qquad f_i(x) = x^2 .
> $$
>
> They are distinct because the domain and codomain are part of a function. They also have different properties ([[§9 Injections, Surjections and Bijections#^ex-9-1|Example §9.1]]): only $f_4$ is a bijection.
>
> *Eccles: Example 8.1.5*

^ex-8-3

> [!example] Example §8.4: Formulae and Their Domains
> A formula must make sense at every point of the domain. $f_1(x) = \dfrac{x^2 + x - 2}{x - 1}$ does not define a function $\R \to \R$, since it gives no value at $x = 1$. **Convention:** when a function on real numbers is given by a formula with no domain or codomain specified, the domain is the set of reals where the formula makes sense and the codomain is $\R$; so here $f_1 : \R - \{1\} \to \R$.
>
> There are two ways to extend $f_1$ to a function with domain $\R$:
> - *rewrite the formula:* for $x \ne 1$, $\dfrac{x^2 + x - 2}{x - 1} = \dfrac{(x - 1)(x + 2)}{x - 1} = x + 2$, and $f_2(x) = x + 2$ defines $f_2 : \R \to \R$ agreeing with $f_1$ on $\R - \{1\}$;
> - *define the missing value explicitly:*
>
> $$
> f_3(x) = \begin{cases} \dfrac{x^2 + x - 2}{x - 1} & x \ne 1, \\ 3 & x = 1, \end{cases} \qquad f_4(x) = \begin{cases} \dfrac{x^2 + x - 2}{x - 1} & x \ne 1, \\ 42 & x = 1. \end{cases}
> $$
>
> The value at a single point may be chosen arbitrarily. Here $f_3 = f_2$ ([[§8 Functions#^def-8-3|Def. §8.3]]), because $f_3(1) = 3 = f_2(1)$ was chosen to match, even though the two are defined differently: a function is determined by its values, not by the process that produces them. On the other hand $f_4 \ne f_2$. For $x \mapsto 1/x$ no rewriting removes the gap at $0$, but explicit definition still works: $g(x) = 1/x$ for $x \ne 0$, $g(0) = 73$, defines $g : \R \to \R$.
>
> *Eccles: Examples 8.1.6, 8.1.7, 8.1.10*

^ex-8-4

> [!example] Example §8.5: Piecewise Definitions Must Be Well-Defined
> **(a)** The **modulus** function $\R \to \R$ (the absolute value of [[§1 The Language of Mathematics#^def-1-4|Def. §1.4]], viewed as a function) is
>
> $$
> |x| = \begin{cases} x & x \ge 0, \\ -x & x \le 0. \end{cases}
> $$
>
> The value at $0$ is given twice, since $0 \ge 0$ and $0 \le 0$; this is allowed because both formulas give $0$ there. A definition by cases is **well-defined** when every point receives exactly one value: the cases cover the domain, and where they overlap the formulas agree.
>
> **(b)** Define $f, g : \R^2 \to \R$ by
>
> $$
> f(x, y) = \frac{x + y}{2} + \frac{|x - y|}{2}, \qquad g(x, y) = \begin{cases} x & x \ge y, \\ y & x \le y. \end{cases}
> $$
>
> *$g$ is well-defined:* by trichotomy every $(x, y)$ has $x \ge y$ or $x \le y$, and when both hold, $x = y$, so the two values $x$ and $y$ agree.
>
> *$f = g$:* if $x \ge y$ then $|x - y| = x - y$, so $f(x, y) = \frac{x + y}{2} + \frac{x - y}{2} = x = g(x, y)$; if $x \le y$ then $|x - y| = y - x$, so $f(x, y) = \frac{x + y}{2} + \frac{y - x}{2} = y = g(x, y)$. Every point is covered by one of these cases. (So $f = g$ is the function $\max(x, y)$.)
>
> *Eccles: Example 8.1.8; Exercise 8.1*

^ex-8-5

> [!remark]- Connections
> - The modulus is the absolute value of [[§3 The Set ℝ of Real Numbers#^def-3-4|451 Def. §3.4]].

> [!definition] Definition §8.3: Equality of Functions
> Two functions $f : X \to Y$ and $g : X \to Y$ are **equal**, written $f = g$, when they have the same value at each point of the domain: $f(x) = g(x)$ for all $x \in X$. Implicit in this is that equal functions have the same domain and the same codomain.
>
> *Eccles: Definition 8.1.9*

^def-8-3

> [!definition] Definition §8.4: Restriction
> Let $f : X \to Y$ and $A \subseteq X$. The **restriction** of $f$ to $A$ is the function $f|A : A \to Y$ given by $(f|A)(a) = f(a)$ for all $a \in A$.
>
> For example, in [[§8 Functions#^ex-8-2|Example §8.2]] $f_1|\{a, b\} = f_2|\{a, b\}$ is the constant function with value $d$; in [[§8 Functions#^ex-8-3|Example §8.3]] $f_2 = f_1|\R^{\geq}$ and $f_4 = f_3|\R^{\geq}$; in [[§8 Functions#^ex-8-4|Example §8.4]] $f_2|(\R - \{1\}) = f_4|(\R - \{1\}) = f_1$.
>
> *Eccles: Definition 8.1.11; Examples 8.1.12*

^def-8-4

> [!remark] Remark: Many Pictures, One Notion
> A table of values, a diagram of arrows, a placing of objects into boxes, a formula, and (below) a graph are all ways of describing a function. Each suits some purposes better than others, and each makes different properties visible; in [[§9 Injections, Surjections and Bijections|§9]], injectivity and surjectivity are read off from each of them. What they share is the defining property: exactly one value at each point of the domain.
>
> *Eccles: Section 8.1*

^rem-8-1

## 8.2 Composition of Functions

> [!definition] Definition §8.5: Composite
> Given functions $f : X \to Y$ and $g : Y \to Z$, the **composite** $g \circ f : X \to Z$ (also written $gf$) is defined by
>
> $$
> (g \circ f)(x) = g(f(x)) \qquad \text{for all } x \in X.
> $$
>
> *Eccles: Definition 8.2.1*

^def-8-5

> [!remark]- Connections
> - Computational version: [[§3 New Functions from Old Functions#^def-3-2|Calc Def. §3.2]] (with worked examples in [[§3 New Functions from Old Functions#^ex-3-5|Calc Ex. §3.5]]).

> [!remark] Remark: The Order in g∘f
> Since values are written $f(x)$, with the function on the left, "apply $f$, then $g$" is written $g \circ f$, in the opposite order to the order of application: $X \xrightarrow{\ f\ } Y \xrightarrow{\ g\ } Z$. Avoid the phrase "the composite of $f$ and $g$" when both orders make sense; write $g \circ f$ or $f \circ g$.
>
> *Eccles: Section 8.2*

^rem-8-2

> [!definition] Definition §8.6: Inclusion Function
> If $A \subseteq X$, the **inclusion function** $i : A \to X$ is given by $i(a) = a$ for all $a \in A$. For any $f : X \to Y$, the composite $f \circ i : A \to Y$ equals the restriction $f|A$, since $(f \circ i)(a) = f(a) = (f|A)(a)$.
>
> *Eccles: Examples 8.2.2(b)*

^def-8-6

> [!example] Example §8.6: Composition Is Not Commutative
> **(a)** Let $f, g : \R \to \R$, $f(x) = x + 1$, $g(x) = x^2$. Then $(g \circ f)(x) = g(x + 1) = (x + 1)^2$, while $(f \circ g)(x) = f(x^2) = x^2 + 1$. These differ (at $x = 1$: $4 \ne 2$), so $g \circ f \ne f \circ g$.
>
> **(b)** Let $f : \R \to \R$, $f(x) = x^2 + 1$, and $g : \R - \{0\} \to \R$, $g(x) = 1/x$. Strictly, $g \circ f$ is not defined, since the codomain of $f$ is not the domain of $g$. But every value of $f$ lies in the domain of $g$ (as $x^2 + 1 \ge 1 > 0$), so $(g \circ f)(x) = g(f(x)) = \dfrac{1}{x^2 + 1}$ still defines a function $\R \to \R$; formally, it is $g \circ f^+$ where $f^+ : \R \to \R - \{0\}$ has the same values as $f$.
>
> *Eccles: Examples 8.2.2(a), (c)*

^ex-8-6

> [!remark]- Connections
> - More worked examples: [[§3 New Functions from Old Functions#^ex-3-5|Calc Ex. §3.5]] (a), where f ∘ g ≠ g ∘ f.

> [!theorem] Proposition §8.1: Associativity and Identities
> Let $f : X \to Y$, $g : Y \to Z$ and $h : Z \to W$. Then
> 1. $(h \circ g) \circ f = h \circ (g \circ f) : X \to W$;
> 2. $f \circ I_X = f = I_Y \circ f : X \to Y$.
>
> So $h \circ g \circ f$ may be written without brackets: composition is **associative**.
>
> *Eccles: Proposition 8.2.3 (the codomain in (1) is printed as $Z$; it is $W$)*

^prop-8-1

> [!proof]+ Proof
> Both sides of each equation are functions with the same domain and codomain, so by [[§8 Functions#^def-8-3|Def. §8.3]] it suffices to compare values. For $x \in X$:
>
> (1) $\big((h \circ g) \circ f\big)(x) = (h \circ g)(f(x)) = h(g(f(x)))$ and $\big(h \circ (g \circ f)\big)(x) = h\big((g \circ f)(x)\big) = h(g(f(x)))$.
>
> (2) $(f \circ I_X)(x) = f(I_X(x)) = f(x)$ and $(I_Y \circ f)(x) = I_Y(f(x)) = f(x)$.

^pf-8-1

*Uses:* [[§8 Functions#^def-8-3|Def. §8.3]], [[§8 Functions#^def-8-5|Def. §8.5]], [[§8 Functions#^def-8-new1|Def. §8.2]]

> [!remark]- Connections
> - Composites of three functions computed from the inside out: [[§3 New Functions from Old Functions#^def-3-2|Calc Def. §3.2]], [[§3 New Functions from Old Functions#^ex-3-5|Calc Ex. §3.5]] (c), (d).
> - Matrix version: [[§11 Matrix Operations#^thm-11-6|235 Thm. §11.6]](a), (e) (matrix multiplication, which is composition of linear maps, is associative, with identity I).

> [!example] Example §8.7: Computing Composites
> Let $f, g : \R \to \R$ be $f(x) = x^3$ and $g(x) = 1 - x$. Then
>
> $$
> (f \circ f)(x) = (x^3)^3 = x^9, \quad (f \circ g)(x) = (1 - x)^3, \quad (g \circ f)(x) = 1 - x^3, \quad (g \circ g)(x) = 1 - (1 - x) = x ,
> $$
>
> so $g \circ g = I_\R$. Where do $f \circ g$ and $g \circ f$ agree?
>
> $$
> (1 - x)^3 = 1 - x^3 \iff 1 - 3x + 3x^2 - x^3 = 1 - x^3 \iff 3x^2 - 3x = 0 \iff x(x - 1) = 0 \iff x \in \{0, 1\}.
> $$
>
> So $\{x \in \R \mid (f \circ g)(x) = (g \circ f)(x)\} = \{0, 1\}$.
>
> *Source: HW3*
> *Eccles: Exercise 8.2 (printed with domain $\R^2$; it should be $\R$)*

^ex-8-7

## 8.3 Sequences

> [!definition] Definition §8.7: Sequence
> A function $f : \Z^+ \to A$ is a **sequence** in the set $A$. Its value $f(n)$ is often written $x_n$, and the sequence $(x_n)$ or $n \mapsto x_n$.
>
> *Eccles: Definition 8.3.1*

^def-8-7

Sequences may be given by formulas ($n \mapsto n^2$, $n \mapsto 1/n$, $n \mapsto 2^n$, $n \mapsto (1 + 1/n)^n$), but the more interesting ones are defined inductively, like the Fibonacci sequence ([[§5 The Induction Principle#^def-5-5|Def. §5.5]]); even $2^n$ and $n!$ are, strictly, inductive definitions ([[§5 The Induction Principle#^def-5-3|Def. §5.3]], [[§5 The Induction Principle#^def-5-4|Def. §5.4]]). A central use of quantifiers is the definition of the limit of a sequence; the simplest case is limit $0$.

> [!definition] Definition §8.8: Null Sequence
> A sequence $f : \Z^+ \to \R$ is **null**, written $\lim f = 0$ or $\displaystyle\lim_{n \to \infty} f(n) = 0$, when
>
> $$
> \forall \varepsilon \in \R^+,\ \exists N \in \Z^+,\ \forall n \in \Z^+,\ \big(n \ge N \Rightarrow |f(n)| < \varepsilon\big).
> $$
>
> *Eccles: Definition 8.3.2*

^def-8-8

> [!remark]- Connections
> - Developed further in: [[§7 Limits of Sequences#^def-7-2|451 Def. §7.2]] (convergence of a sequence; null means converging to $0$), with sequences as functions on a set of integers in [[§7 Limits of Sequences#^def-7-1|451 Def. §7.1]].

> [!example] Example §8.8: Two Null Sequences
> **(a)** $n \mapsto 1/n$ is null. **(b)** $n \mapsto 1/\sqrt{n}$ is null.
>
> **Constructing a proof.** For (b) we must prove $\forall \varepsilon \in \R^+,\ \exists N \in \Z^+,\ \forall n \in \Z^+,\ (n \ge N \Rightarrow 1/\sqrt{n} < \varepsilon)$, noting $|1/\sqrt{n}| = 1/\sqrt{n}$. So, given $\varepsilon \in \R^+$, find out when the conclusion holds:
>
> $$
> \frac{1}{\sqrt{n}} < \varepsilon \iff \frac{1}{n} < \varepsilon^2 \iff n > \frac{1}{\varepsilon^2}.
> $$
>
> Any positive integer $N > 1/\varepsilon^2$ will do: $\varepsilon = 1$ needs $N > 1$, $\varepsilon = \frac12$ needs $N > 4$, $\varepsilon = \frac{1}{100}$ needs $N > 10000$. The smaller $\varepsilon$, the larger $N$ must be; $N$ depends on $\varepsilon$, as the order $\forall \varepsilon\, \exists N$ allows ([[§7 Quantifiers#^rem-7-4|§7, remark on statements with two quantifiers]]).
>
> **Proof of (a).** Let $\varepsilon \in \R^+$. Choose a positive integer $N > 1/\varepsilon$ (one exists because the positive integers are unbounded in $\R$). If $n \in \Z^+$ and $n \ge N$, then $n > 1/\varepsilon$, so $|1/n| = 1/n < \varepsilon$.
>
> **Proof of (b).** Let $\varepsilon \in \R^+$ and choose $N \in \Z^+$ with $N > 1/\varepsilon^2$. If $n \ge N$ then $n > 1/\varepsilon^2$, so $1/n < \varepsilon^2$ and, taking positive square roots, $1/\sqrt{n} < \varepsilon$.
>
> *Source: HW3 (part (a))*
> *Eccles: Exercise 8.4; Example 8.3.3*

^ex-8-8

> [!remark]- Connections
> - The existence of an integer $N > 1/\varepsilon$ is the Archimedean property, [[§4 The Completeness Axiom#^thm-4-5|451 Thm. §4.5]].

## 8.4 The Image of a Function

> [!definition] Definition §8.9: Image of a Function
> Given $f : X \to Y$, the **image** of $f$ is the subset of the codomain consisting of the values of $f$:
>
> $$
> \operatorname{Im} f = \{f(x) \mid x \in X\} \subseteq Y .
> $$
>
> So $f$ gives a constructive definition of the set $\operatorname{Im} f$ ([[§6 The Language of Set Theory#^def-6-2|Def. §6.2]]). For example, $x \mapsto x^2$ on $\R$ has image $\R^{\geq}$; in particular $-1 \notin \operatorname{Im} f$.
>
> *Eccles: Definition 8.4.1*

^def-8-9

> [!remark]- Connections
> - Same notion, called the range: [[§1 Countability and Set Theory#^def-1-5|551 Def. §1.5]].
> - The range in Stewart: [[§1 Four Ways to Represent a Function#^def-1-1|Calc Def. §1.1]].
> - For linear transformations: the range in [[§8 Introduction to Linear Transformations#^def-8-new1|235 Def. §8.1]]; for a matrix it is the column space, [[§24 Null Spaces, Column Spaces, and Linear Transformations#^def-24-2|235 Def. §24.2]].

> [!example] Example §8.9: Functions With Prescribed Images
> Functions $f_i : \R \to \R$ with:
> - $\operatorname{Im} f_1 = \R$: $f_1 = I_\R$.
> - $\operatorname{Im} f_2 = \R^+$: $f_2(x) = x$ for $x > 0$ and $f_2(x) = 1$ for $x \le 0$. Every value is positive, and every $y > 0$ equals $f_2(y)$.
> - $\operatorname{Im} f_3 = \R - \Z$: $f_3(x) = x$ for $x \notin \Z$ and $f_3(x) = x + \frac12$ for $x \in \Z$. Values at non-integers are non-integers; for $n \in \Z$, $n + \frac12$ lies strictly between the consecutive integers $n$ and $n + 1$, so is not an integer; and every $y \notin \Z$ equals $f_3(y)$.
> - $\operatorname{Im} f_4 = \Z$: $f_4(x) = x$ for $x \in \Z$ and $f_4(x) = 0$ for $x \notin \Z$.
>
> In each case the proof that $\operatorname{Im} f_i$ is the given set $S$ has two halves, as for any equality of sets: every value lies in $S$, and every element of $S$ is a value.
>
> *Eccles: Exercise 8.3*

^ex-8-9

## 8.5 The Graph of a Function

> [!definition] Definition §8.10: Graph of a Function
> The **graph** of $f : X \to Y$ is the subset of $X \times Y$
>
> $$
> G_f = \{(x, y) \in X \times Y \mid y = f(x)\} = \{(x, f(x)) \mid x \in X\}.
> $$
>
> For $X, Y \subseteq \R$ this is the usual graph of calculus.
>
> *Eccles: Definition 8.5.1; Remarks 8.5.2*

^def-8-10

> [!remark]- Connections
> - Stewart's definition: [[§1 Four Ways to Represent a Function#^def-1-2|Calc Def. §1.2]].

> [!theorem] Proposition §8.2: Graphs Determine Functions
> 1. If $f : X \to Y$, then for each $x_0 \in X$ the "column" $\{x_0\} \times Y$ meets $G_f$ in exactly one point, namely $(x_0, f(x_0))$.
> 2. If $f, g : X \to Y$ and $G_f = G_g$, then $f = g$.
> 3. Conversely, if $G \subseteq X \times Y$ meets each column $\{x_0\} \times Y$ in exactly one point, then $G = G_f$ for exactly one function $f : X \to Y$.
>
> In particular, not every subset of $X \times Y$ is a graph.
>
> *Eccles: Section 8.5 (after Example 8.5.3)*

^prop-8-2

> [!proof]+ Proof
> (1) $(x_0, f(x_0)) \in G_f$. If $(x_0, y) \in G_f$, then $y = f(x_0)$; so this is the only point of $G_f$ in the column.
>
> (2) For $x_0 \in X$, $(x_0, f(x_0)) \in G_f = G_g$, so $f(x_0) = g(x_0)$. Hence $f = g$ by [[§8 Functions#^def-8-3|Def. §8.3]].
>
> (3) For $x_0 \in X$ let $f(x_0)$ be the second coordinate of the unique point of $G$ in $\{x_0\} \times Y$. This assigns a unique element of $Y$ to each $x_0 \in X$, so it is a function $f : X \to Y$. For $(x, y) \in X \times Y$: if $(x, y) \in G$, it is the point of $G$ in the column of $x$, so $y = f(x)$ and $(x, y) \in G_f$; if $y = f(x)$ then $(x, y)$ is that point, so $(x, y) \in G$. Thus $G = G_f$, and $f$ is unique by (2).

^pf-8-2

*Uses:* [[§8 Functions#^def-8-10|Def. §8.10]], [[§8 Functions#^def-8-3|Def. §8.3]], [[§8 Functions#^def-8-1|Def. §8.1]], [[§7 Quantifiers#^def-7-5|Def. §7.5]], [[§7 Quantifiers#^def-7-new1|Def. §7.5]]

> [!remark]- Connections
> - Computational version: the vertical line test, [[§1 Four Ways to Represent a Function#^thm-1-1|Calc Thm. §1.1]].

> [!remark] Remark: A Function Is Its Graph
> [[§8 Functions#^def-8-1|Definition §8.1]] rests on the undefined word "assignment". In more advanced mathematics a function $X \to Y$ is *defined* to be a subset of $X \times Y$ in which each element of $X$ occurs as the first coordinate of exactly one element; by [[§8 Functions#^prop-8-2|Proposition §8.2]] this captures exactly the same objects, and it reduces functions to sets.
>
> *Eccles: footnote to Section 8.5*

^rem-8-3

> [!example] Example §8.10: Which Subsets Are Graphs?
> Let $X = \{a, b, c, d\}$ and $Y = \{w, x, y, z\}$, and consider four subsets of $X \times Y$ (given in Eccles as dot diagrams), listed here by their elements:
>
> | | subset of $X \times Y$ | graph of a function? |
> |---|---|---|
> | (i) | $(a,z), (b,y), (c,z), (d,x)$ | yes: $a \mapsto z,\ b \mapsto y,\ c \mapsto z,\ d \mapsto x$ |
> | (ii) | $(a,z), (b,y), (d,x)$ | no: the column of $c$ contains no point, so no value is given at $c$ |
> | (iii) | $(a,z), (b,y), (b,w), (c,x), (d,z)$ | no: the column of $b$ contains two points, so two values are given at $b$ |
> | (iv) | $(a,y), (b,z), (c,w), (d,x)$ | yes: $a \mapsto y,\ b \mapsto z,\ c \mapsto w,\ d \mapsto x$ |
>
> This is [[§8 Functions#^prop-8-2|Proposition §8.2]] at work: a subset is a graph exactly when each column contains exactly one point. Similarly, the graphs of $f_1$ and $f_2$ of [[§8 Functions#^ex-8-2|Example §8.2]] are $\{(a,d), (b,d), (c,d)\}$ and $\{(a,d), (b,d), (c,e)\}$.
>
> *Source: HW3*
> *Eccles: Exercise 8.5; Example 8.5.3*

^ex-8-10
