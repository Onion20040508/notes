---
type: section
subject: "[[Functional Analysis]]"
chapter: 2
section: 5
tags: [functional-analysis, math556]
---
← [[§4 Statement and Motivation]] · ↑ [[· 2 The Hahn–Banach Theorem]] · [[§6 Convex Sets and the Gauge]] →

*Stage: algebra — Thread: functionals. One-step extension, then Zorn's lemma.*

## Why Linear Functionals

Before the proof, two remarks on why the set of linear functionals on $X$ is worth studying at all.

> [!remark] Remark: Linear Functionals Replace the Dot Product
> On $\mathbb{R}^n$ every linear functional is $x \mapsto a \cdot x$ for a unique $a \in \mathbb{R}^n$, so vectors and linear functionals are in one-to-one correspondence $a \leftrightarrow \ell_a$. Statements about the dot product translate into statements about linear functionals: $a \cdot x = 0$ says $x$ is perpendicular to $a$, and “$a \cdot x = 0$ for every $a$ implies $x = 0$” (take $a = x$) says that a vector perpendicular to everything is zero.
>
> A general linear space has no dot product. But it does have linear functionals, and the correspondence above suggests using them as the substitute: “$x$ is perpendicular to $\ell$” means $\ell(x) = 0$, and the question of whether “$\ell(x) = 0$ for all $\ell$ forces $x = 0$” becomes a question about how many linear functionals exist. The [[§4 Statement and Motivation#^thm-4-2|Hahn–Banach theorem]] is what guarantees there are enough of them.

^rem-5-1

> [!remark]- Connections
> - Every functional on $\mathbb{R}^n$ is a dot product: [[§2 Linear Maps, Convexity, and Linear Functionals#^ex-2-2|Ex. §2.2]]; on finite-dimensional inner product spaces [[Riesz representation theorem|LADR 6.42]]; on Hilbert spaces (bounded functionals) [[§23 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-23-2|§23.2]].

> [!remark] Remark: Convergence Without Topology
> A linear space carries no notion of distance, so for a sequence $\{x_n\} \subset X$ the statement “$x_n \to x$” has no meaning. But for a linear functional $\ell$, the sequence $\ell(x_n)$ is a sequence of scalars, and convergence of scalars is understood. So linear functionals let one speak of a sequence in $X$ converging, at least in the sense that $\ell(x_n) \to \ell(x)$ for the functionals $\ell$ under consideration. This will be developed later in the course ([[§18 Compactness and the Unit Ball#^rem-18-4|weak convergence]]).

^rem-5-2

## A First Application: One Functional per Vector

The theorem is a *construction* device. The simplest use:

> [!example] Example §5.1: Extending from a Line
> Let $y_0 \in X$, $y_0 \neq 0$, and let $Y = \operatorname{span}\{y_0\} = \{ a y_0 \mid a \in \mathbb{R} \}$. Define $\ell$ on $Y$ by
>
> $$
> \ell(a y_0) = a, \qquad \text{i.e. } \ell(y_0) = 1.
> $$
>
> This is a linear functional on the one-dimensional subspace $Y$. Given any positive homogeneous subadditive $p$ on $X$ with $\ell(y) \le p(y)$ on $Y$, [[§4 Statement and Motivation#^thm-4-2|Hahn–Banach]] extends $\ell$ to a linear functional $L : X \to \mathbb{R}$ with $L \le p$ on all of $X$. (One can prescribe any value at $y_0$, not only $1$; the normalization is a convenience.)
>
> Thus associated to every nonzero vector of $X$ there is at least one linear functional on $X$ taking a prescribed nonzero value there. The extension is not unique.

^ex-5-1

> [!remark]- Connections
> - The same construction, with $p$ the gauge of a convex set, is Steps 2–3 of the separation theorem: [[§7 The Hyperplane Separation Theorem#^pf-7-1|§7.1]].

## The One-Step Extension

The whole proof is a single computation: extend $\ell$ by one dimension while keeping $\ell \le p$. Everything else is bookkeeping.

> [!theorem] Lemma §5.1: One-Step Extension
> Let $X$, $p$, $Y$, $\ell$ be as in Theorem [[§4 Statement and Motivation#^thm-4-2|§4.2]], and suppose $Y \subsetneq X$. Fix $x_0 \in X \setminus Y$ and let
>
> $$
> Z = \operatorname{span}\{x_0, Y\} = \{ a x_0 + y \mid a \in \mathbb{R},\ y \in Y \}.
> $$
>
> Then $\ell$ extends to a linear functional on $Z$: there is a linear $L : Z \to \mathbb{R}$ with $L|_Y = \ell$ and $L(z) \le p(z)$ for all $z \in Z$.
>
> ![[m556-4-1.svg]]
> *Pictured for $\dim Y = 1$: $Y$ is a line, $x_0$ is off it, and $Z$ is the plane they span. Every element of $Z$ is $a x_0 + y$ for a unique $a$ and $y$.*
>
> *Lax: §3.1, proof of Thm 1*

^lem-5-1

> [!proof]+ Proof
> **Step 1: Reduction to a single number.** First, $Z$ is as described: sums and scalar multiples of elements $a x_0 + y$ are again of that form, so the set of such elements is a subspace containing $x_0$ and $Y$, and it is clearly the smallest one. Moreover the representation $z = a x_0 + y$ is unique: if $a x_0 + y = a' x_0 + y'$ then $(a - a') x_0 = y' - y \in Y$, and since $x_0 \notin Y$ this forces $a = a'$, hence $y = y'$.
>
> Any linear extension $L$ of $\ell$ to $Z$ must satisfy
>
> $$
> L(a x_0 + y) = a\, L(x_0) + \ell(y),
> $$
>
> and $\ell(y)$ is already known. So the extension is determined by the single real number $c := L(x_0)$, and conversely any choice of $c$ defines a linear functional on $Z$ by this formula (well defined by uniqueness of the representation). The problem is to choose $c$ so that
>
> $$
> L(a x_0 + y) \le p(a x_0 + y) \qquad \text{for all } y \in Y,\ a \in \mathbb{R}. \tag{2.1}
> $$
>
> **Step 2: It suffices to treat $a = 1$ and $a = -1$.** We claim it is enough to arrange
>
> $$
> L(x_0 + y) \le p(x_0 + y) \qquad \text{for all } y \in Y, \tag{1}
> $$
>
> $$
> L(-x_0 + y') \le p(-x_0 + y') \qquad \text{for all } y' \in Y. \tag{2}
> $$
>
> The reason is positive homogeneity: $p(ax) = a\,p(x)$ lets a positive scalar be pulled out of $p$, and linearity lets any scalar be pulled out of $L$, so the case of general $a > 0$ reduces to $a = 1$ and the case $a < 0$ reduces to $a = -1$. We cannot pull a negative scalar through $p$, which is why both signs are needed. The verification is Step 5.
>
> **Step 3: What (1) and (2) say about $c$.** By linearity of $L$ and $L|_Y = \ell$,
>
> $$\begin{aligned}
> \text{(1)} &\iff c + \ell(y) \le p(x_0 + y) \ \ \forall y \in Y \iff c \le p(x_0 + y) - \ell(y) \ \ \forall y \in Y, \\
> \text{(2)} &\iff -c + \ell(y') \le p(-x_0 + y') \ \ \forall y' \in Y \iff \ell(y') - p(-x_0 + y') \le c \ \ \forall y' \in Y.
> \end{aligned}$$
>
> Together:
>
> $$
> \ell(y') - p(-x_0 + y') \;\le\; c \;\le\; p(x_0 + y) - \ell(y) \qquad \text{for all } y, y' \in Y. \tag{3}
> $$
>
> So if $c = L(x_0)$ can be chosen at all, it must satisfy (3). Note that both outer expressions are well defined: $\ell$ is given on $Y$, and $p$ is given on $X$. The question is whether the two sides leave any room for $c$.
>
> **Step 4: The sandwich is nonempty.** We show
>
> $$
> \ell(y') - p(-x_0 + y') \le p(x_0 + y) - \ell(y) \qquad \text{for all } y, y' \in Y. \tag{4}
> $$
>
> Moving the $\ell$-terms to the left and the $p$-terms to the right, (4) is equivalent to
>
> $$
> \ell(y') + \ell(y) \le p(-x_0 + y') + p(x_0 + y).
> $$
>
> Now $y' + y \in Y$, so by linearity of $\ell$ on $Y$, the hypothesis $\ell \le p$ on $Y$, and subadditivity of $p$,
>
> $$
> \ell(y') + \ell(y) = \ell(y' + y) \le p(y' + y) = p\bigl((y' - x_0) + (x_0 + y)\bigr) \le p(y' - x_0) + p(x_0 + y),
> $$
>
> which is the desired inequality. Hence (4) holds.
>
> Fix $y \in Y$ and take the supremum over $y' \in Y$ on the left of (4): the set $\{\ell(y') - p(-x_0 + y') : y' \in Y\}$ is nonempty and bounded above by $p(x_0 + y) - \ell(y)$, so
>
> $$
> c := \sup_{y' \in Y} \bigl( \ell(y') - p(-x_0 + y') \bigr)
> $$
>
> is a finite real number with $c \le p(x_0 + y) - \ell(y)$ for every $y \in Y$. Being a supremum, $c \ge \ell(y') - p(-x_0 + y')$ for every $y' \in Y$. Thus $c$ satisfies (3). (Equally one could take the infimum of the right-hand side of (4) over $y$, or any number in between; the choice is not unique.)
>
> We now *define* $L(x_0) := c$ and, for $a \in \mathbb{R}$, $y \in Y$,
>
> $$
> L(a x_0 + y) := a\, c + \ell(y).
> $$
>
> By Step 1 this $L$ is a well-defined linear functional on $Z$ extending $\ell$, and by Step 3 it satisfies (1) and (2).
>
> **Step 5: Verification of (2.1) for all $a$.** For $a = 0$, $\ell(y) \le p(y)$ is the hypothesis.
>
> *Case $a > 0$.* Since $y / a \in Y$, linearity of $L$, (1), and positive homogeneity of $p$ give
>
> $$
> L(a x_0 + y) = a\, L\Bigl(x_0 + \frac{y}{a}\Bigr) \le a\, p\Bigl(x_0 + \frac{y}{a}\Bigr) = p(a x_0 + y).
> $$
>
> *Case $a < 0$.* Now $-a > 0$ is the scalar that can be pulled through $p$. Since $y / (-a) \in Y$, linearity, (2), and positive homogeneity give
>
> $$
> L(a x_0 + y) = (-a)\, L\Bigl(-x_0 + \frac{y}{-a}\Bigr) \le (-a)\, p\Bigl(-x_0 + \frac{y}{-a}\Bigr) = p(a x_0 + y).
> $$
>
> This proves (2.1), and $\ell$ has been extended to $L$ on $Z$, one dimension larger than $Y$.

^pf-5-1

*Uses:* [[§4 Statement and Motivation#^def-4-1|Def. §4.1]], [[§1 Linear Spaces#^def-1-5|Def. §1.5]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[Completeness Axiom|451 §4.4]]

![[m556-4-2.svg]]
*Steps 3–4 on the real line. Each red number $\ell(y') - p(-x_0 + y')$ is a lower bound for $c = L(x_0)$ and each blue number $p(x_0 + y) - \ell(y)$ an upper bound. Inequality (4) says every red number lies to the left of every blue one, so the supremum of the red numbers is at most the infimum of the blue ones, and the green interval between them is nonempty; any $c$ in it satisfies (3). The proof takes the left endpoint.*

> [!remark]- Connections
> - The same one-step pattern for complements: [[§1 Linear Spaces#^lem-1-7|§1.7]]; as a technique: [[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]].

> [!remark] Remark: On the Choice of $L(x_0)$
> A question in lecture: does taking a supremum preserve linearity? The supremum is not used to define a function; it produces a single real number $c$, which is then assigned as the value $L(x_0)$. Linearity is imposed afterwards by the formula $L(a x_0 + y) = a c + \ell(y)$. Any number in the interval (3) would do; the supremum is merely a convenient way of exhibiting one.
>
> Also note the discipline in Step 3: the conditions (1), (2) were converted to conditions on $c$ by *equivalences*, not by one-sided estimates. Applying subadditivity too early would have thrown away information and made the interval for $c$ harder to see.

^rem-5-3

## Completing the Proof: Zorn's Lemma

> [!theorem] Theorem §5.2: Zorn's Lemma
> Let $(P, \le)$ be a nonempty partially ordered set in which every chain (totally ordered subset) has an upper bound in $P$. Then $P$ has a maximal element, i.e. an $m \in P$ with no $x \in P$ satisfying $m < x$.
>
> *Lax: §3.1, proof of Thm 1*

^thm-5-2

> [!remark]- Connections
> - Also used for complements, [[§1 Linear Spaces#^prop-1-8|§1.8]], and for orthonormal bases, [[§24 Orthonormal Sets and Bases#^thm-24-12|§24.12]]; the pattern: [[Functional Analysis Problem-Solving Techniques#^rem-t3|Technique 3]].

Zorn's lemma is equivalent to the axiom of choice and is taken as an axiom; no proof is given. Wu stated in lecture that the partial-order argument would not be carried out on the board; it is written out here.

> [!proof]+ Proof of Theorem [[§4 Statement and Motivation#^thm-4-2|§4.2]]
> (Wu: “By Zorn's lemma, we're done.” The argument is written out here.) If $Y = X$ there is nothing to do, so assume $Y \subsetneq X$. Let $P$ be the set of pairs $(Z, \ell_Z)$ with $Y \subset Z \subset X$ a linear subspace and $\ell_Z : Z \to \mathbb{R}$ a linear functional extending $\ell$ with $\ell_Z \le p$ on $Z$, ordered by extension: $(Z, \ell_Z) \le (Z', \ell_{Z'})$ iff $Z \subset Z'$ and $\ell_{Z'}|_Z = \ell_Z$. Then $(Y, \ell) \in P$, so $P \neq \varnothing$.
>
> *Chains have upper bounds.* Given a chain $\{(Z_i, \ell_i)\}_{i \in I}$, let $Z^{\ast} = \bigcup_i Z_i$ and define $\ell^{\ast}(z) = \ell_i(z)$ for any $i$ with $z \in Z_i$. Since the chain is nested, any two elements of $Z^{\ast}$ lie in a common $Z_i$, so $Z^{\ast}$ is a subspace and $\ell^{\ast}$ is well defined and linear; $\ell^{\ast} \le p$ on $Z^{\ast}$ because it holds on each $Z_i$. Thus $(Z^{\ast}, \ell^{\ast}) \in P$ is an upper bound.
>
> *Conclusion.* By Zorn's lemma $P$ has a maximal element $(Z_m, \ell_m)$. If $Z_m \neq X$, Lemma [[§5 Proof of the Hahn–Banach Theorem#^lem-5-1|§5.1]] (with $Z_m$ in place of $Y$) extends $\ell_m$ to a strictly larger subspace keeping $\ell \le p$, contradicting maximality. Hence $Z_m = X$, and $L := \ell_m$ is the required extension.

^pf-4-2

*Uses:* [[§5 Proof of the Hahn–Banach Theorem#^thm-5-2|§5.2]], [[§5 Proof of the Hahn–Banach Theorem#^lem-5-1|§5.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]]

> [!remark] Remark
> Lemma [[§5 Proof of the Hahn–Banach Theorem#^lem-5-1|§5.1]] contains all the analysis; Zorn's lemma only says “repeat until finished” in a way that is legitimate when $X$ has uncountable dimension. In [[§24 Orthonormal Sets and Bases#^def-24-5|separable]] normed spaces (later) the extension can instead be built by ordinary induction along a countable dense sequence.

^rem-5-4
