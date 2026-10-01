---
type: section
subject: "[[Functional Analysis]]"
chapter: 5
section: 19
tags: [functional-analysis, math556]
---
← [[§18 Projection and Orthogonal Decomposition]] · ↑ [[· 5 Inner Product Spaces]] · [[§20 Orthonormal Sets and Bases]] →

*Stage: inner products — Thread: functionals. On a Hilbert space every bounded functional is an inner product.*

## Bounded Linear Functionals

On $\mathbb{R}^n$ every linear functional is $x \mapsto a \cdot x$ for a unique vector $a$ (Example [[§2 Linear Maps, Convexity, and Linear Functionals#^ex-2-2|§2.2]]). The Riesz representation theorem says the same is true in any Hilbert space, once “linear functional” is replaced by the right notion.

> [!definition] Definition §19.1: Bounded Linear Functional
> Let $(X, \|\cdot\|)$ be a normed linear space over $\mathbb{F}$. A linear functional $\ell : X \to \mathbb{F}$ is **bounded** if there is a constant $c > 0$ such that
>
> $$
> |\ell(x)| \le c\,\|x\| \qquad \text{for all } x \in X .
> $$
>
> *Lax: §6.3, (14)*

^def-19-1

> [!remark]- Connections
> - The general notion for maps between normed spaces: [[§21 Boundedness and Continuity#^def-21-2|Def. §21.2]]; the dual space of bounded functionals: [[§22 Bras, Kets, and the Riesz Map#^def-22-1|Def. §22.1]].

> [!remark] Remark: Why Boundedness
> On $\mathbb{R}^n$ every linear functional is bounded: $|a \cdot x| \le \|a\|\,\|x\|$ by [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|Cauchy–Schwarz]], so $c = \|a\|$ works. More generally every linear functional on a finite-dimensional normed space is bounded (with a basis $e_1, \ldots, e_n$ and $x = \sum_i a_i e_i$, $|\ell(x)| \le \sum_i |a_i|\,|\ell(e_i)| \le \bigl(\max_i |\ell(e_i)|\bigr)\|x\|_1$, and $\|\cdot\|_1$ is equivalent to the given norm by Theorem [[§10 New Normed Spaces from Old#^thm-10-3|§10.3]]). In infinite dimensions this fails — the [[§8 Normed Linear Spaces#^rem-8-3|remark]] after Proposition [[§8 Normed Linear Spaces#^prop-8-4|§8.4]] and the [[§17 Cauchy–Schwarz and the Induced Norm#^rem-17-3|remark]] after Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-4|§17.4]] both mention functionals built from a Hamel basis that are unbounded on every ball — so boundedness is a genuine hypothesis, and it is the one that makes the finite-dimensional picture survive. “Bounded” does not mean bounded as a function: a nonzero linear functional is never bounded on all of $X$, since $\ell(nx) = n\ell(x)$; it means bounded on the unit ball.

^rem-19-1

> [!theorem] Proposition §19.1: Bounded Means Continuous
> For a linear functional $\ell$ on a normed linear space $X$, the following are equivalent:
> - (i) $\ell$ is bounded;
> - (ii) $\ell$ is continuous on $X$ (if $x_n \to x$ then $\ell(x_n) \to \ell(x)$);
> - (iii) $\ell$ is continuous at $0$.

^prop-19-1

> [!proof]+ Proof
> (Not covered in lecture.) (i)$\Rightarrow$(ii): $|\ell(x_n) - \ell(x)| = |\ell(x_n - x)| \le c\|x_n - x\| \to 0$. (ii)$\Rightarrow$(iii) is trivial. (iii)$\Rightarrow$(i): if $\ell$ is not bounded, then for each $n$ there is $x_n$ with $|\ell(x_n)| > n\|x_n\|$, so $x_n \neq 0$; put $z_n = x_n / (n\|x_n\|)$. Then $\|z_n\| = 1/n \to 0$, so $z_n \to 0$, while $|\ell(z_n)| = |\ell(x_n)| / (n\|x_n\|) > 1$, so $\ell(z_n) \not\to 0 = \ell(0)$, contradicting (iii).

^pf-19-1

*Uses:* [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|Def. §19.1]], [[§8 Normed Linear Spaces#^def-8-1|Def. §8.1]], [[§8 Normed Linear Spaces#^def-8-4|Def. §8.4]]

> [!remark]- Connections
> - The same statement for linear maps, proved again in Chapter 6: [[§21 Boundedness and Continuity#^prop-21-2|§21.2]].

## The Riesz Representation Theorem

> [!theorem] Theorem §19.2: Riesz Representation Theorem
> Let $H$ be a Hilbert space over $\mathbb{F}$.
> - (1) For every $a \in H$, the map $\ell_a : H \to \mathbb{F}$, $\ell_a(x) = (x, a)$, is a bounded linear functional on $H$.
> - (2) Conversely, for every bounded linear functional $\ell : H \to \mathbb{F}$ there is a unique $a \in H$ such that
>
> $$
> \ell(x) = (x, a) \qquad \text{for all } x \in H .
> $$
>
> *Lax: §6.3, Thm 4*

^thm-19-2

> [!remark]- Connections
> - The finite-dimensional home: [[Riesz representation theorem|LADR 6.42]], revisited through orthogonal projection in [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-58|LADR 6.58]].
> - The map $a \mapsto \ell_a$ as an isometry onto the dual, and its bra–ket reading: [[§22 Bras, Kets, and the Riesz Map#^thm-22-2|§22.2]].

> [!remark] Remark: Reading the Statement
> Part (1) is the easy direction and holds in any inner product space. Part (2) is the content: on a Hilbert space there are *no other* bounded linear functionals than the ones given by inner products, exactly as on $\mathbb{R}^n$. Wu's example: on $L^2$, every bounded linear functional is $f \mapsto \int f\,\bar{g}$ for a unique $g \in L^2$. The vector is on the *second* slot because the functional must be linear in $x$, and the inner product is linear in its first argument; with the physicists' convention it would be $(a, x)$.

^rem-19-2

> [!proof]+ Proof of (1)
> Linearity of $\ell_a$ in $x$ is linearity of the inner product in its first argument. Boundedness is Cauchy–Schwarz (Theorem [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]]): $|\ell_a(x)| = |(x, a)| \le \|a\|\,\|x\|$, so $c = \|a\|$ works.

^pf-19-2

*Uses:* [[§16 Definition and Examples#^def-16-1|Def. §16.1]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|§17.1]], [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|Def. §19.1]]

The idea of the proof comes from $\mathbb{R}^n$: there $\ell(x) = x \cdot a$, the set $\{\ell = 0\}$ is a hyperplane, and $a$ is a normal vector to it. So one studies the null set of $\ell$ and looks for a vector perpendicular to it. Two facts about the null set are needed first; they are separated out as lemmas.

> [!theorem] Lemma §19.3: The Kernel of a Bounded Functional is Closed
> Let $\ell$ be a bounded linear functional on a normed linear space $X$. Then its **kernel** (or null set)
>
> $$
> N = \ker \ell = \{ y \in X : \ell(y) = 0 \}
> $$
>
> is a closed linear subspace of $X$.

^lem-19-3

> [!proof]+ Proof
> *Subspace.* If $y_1, y_2 \in N$ and $a, b \in \mathbb{F}$, then $\ell(ay_1 + by_2) = a\ell(y_1) + b\ell(y_2) = 0$.
>
> *Closed.* Let $y_n \in N$ with $y_n \to y_0$. Since $\ell$ is bounded, $|\ell(x)| \le M\|x\|$ for some $M$ and all $x$, so
>
> $$
> |\ell(y_n) - \ell(y_0)| = |\ell(y_n - y_0)| \le M\|y_n - y_0\| \to 0 .
> $$
>
> As $\ell(y_n) = 0$ for all $n$, this gives $\ell(y_0) = 0$, i.e. $y_0 \in N$.

^pf-19-3

*Uses:* [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^def-19-1|Def. §19.1]], [[§1 Linear Spaces#^def-1-2|Def. §1.2]], [[§8 Normed Linear Spaces#^def-8-6|Def. §8.6]], [[§8 Normed Linear Spaces#^prop-8-5|§8.5]]

This is the only place in the proof where boundedness is used; by Proposition [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^prop-19-1|§19.1]] it amounts to continuity of $\ell$.

> [!theorem] Lemma §19.4: The Kernel Has Codimension One
> Let $H$ be a Hilbert space, $\ell \neq 0$ a bounded linear functional on $H$, and $N = \ker \ell$. Then $N^\perp \neq \{0\}$, and for every nonzero $x_0 \in N^\perp$:
> - (a) $\ell(x_0) \neq 0$;
> - (b) $N^\perp = \{ k x_0 : k \in \mathbb{F} \}$, so $N^\perp$ is one-dimensional;
> - (c) every $x \in H$ can be written as $x = k x_0 + y$ with $k = \ell(x)/\ell(x_0) \in \mathbb{F}$ and $y \in N$.
>
> *Lax: §6.3, Lemma 5(i)*

^lem-19-4

> [!proof]+ Proof
> By Lemma [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-3|§19.3]], $N$ is a closed linear subspace, and $N \neq H$ because $\ell \neq 0$. By Theorem [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]], $H = N \oplus N^\perp$; if $N^\perp$ were $\{0\}$ this would give $H = N$. So $N^\perp \neq \{0\}$. Fix $0 \neq x_0 \in N^\perp$.
>
> (a) If $\ell(x_0) = 0$ then $x_0 \in N \cap N^\perp = \{0\}$ (a vector orthogonal to itself is $0$), contrary to the choice of $x_0$.
>
> (b) Let $x_1 \in N^\perp$ and put $k = \ell(x_1)/\ell(x_0)$, a quotient of two scalars, so $k \in \mathbb{F}$. Then $\ell(x_1) = k\,\ell(x_0)$, so $\ell(x_1 - k x_0) = 0$ and $x_1 - k x_0 \in N$. But also $x_1 - k x_0 \in N^\perp$, a linear subspace (Proposition [[§18 Projection and Orthogonal Decomposition#^prop-18-3|§18.3]]). Hence $x_1 - k x_0 \in N \cap N^\perp = \{0\}$, i.e. $x_1 = k x_0$. Conversely every $k x_0$ lies in $N^\perp$.
>
> (c) With $k = \ell(x)/\ell(x_0)$ and $y = x - k x_0$, linearity gives $\ell(y) = \ell(x) - k\,\ell(x_0) = 0$, so $y \in N$.

^pf-19-4

*Uses:* [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-3|§19.3]], [[§18 Projection and Orthogonal Decomposition#^thm-18-4|§18.4]], [[§18 Projection and Orthogonal Decomposition#^prop-18-3|§18.3]], [[§18 Projection and Orthogonal Decomposition#^def-18-1|Def. §18.1]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]]

> [!remark] Remark
> Two points raised in lecture. The step $k = \ell(x_1)/\ell(x_0)$ may look like dividing vectors, but it is not: $\ell(x_1)$ and $\ell(x_0)$ are numbers, and the vector identity $x_1 = kx_0$ is obtained afterwards from $N \cap N^\perp = \{0\}$. And a student asked why this shows $\dim N^\perp = 1$: an arbitrary element $x_1$ of $N^\perp$ was shown to be a multiple of one fixed nonzero $x_0$.

^rem-19-3

> [!proof]+ Proof of (2)
> If $\ell = 0$, then $\ell(x) = (x, 0)$ for all $x$, so $a = 0$ works. Assume $\ell \neq 0$, let $N = \ker \ell$, and fix $0 \neq x_0 \in N^\perp$ (Lemma [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]]).
>
> *Finding $a$.* Consider the bounded linear functional $\ell_1(x) = (x, x_0)$. For $x = k x_0 + y$ as in Lemma [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]](c),
>
> $$
> \ell_1(x) = k(x_0, x_0) + (y, x_0) = k\,\|x_0\|^2, \qquad \ell(x) = k\,\ell(x_0) + \ell(y) = k\,\ell(x_0),
> $$
>
> since $(y, x_0) = 0$ ($y \in N$, $x_0 \in N^\perp$) and $\ell(y) = 0$. The two differ by the constant factor $\ell(x_0)/\|x_0\|^2$. This suggests
>
> $$
> a = \frac{\overline{\ell(x_0)}}{\|x_0\|^2}\, x_0 ,
> $$
>
> the conjugate being needed because the inner product is conjugate-linear in its second argument.
>
> *Verification.* For $x = k x_0 + y$ as above, using $(x, c\,x_0) = \bar{c}\,(x, x_0)$,
>
> $$
> (x, a) = \frac{\ell(x_0)}{\|x_0\|^2}\,(k x_0 + y,\, x_0) = \frac{\ell(x_0)}{\|x_0\|^2}\, k\,\|x_0\|^2 = k\,\ell(x_0) = \ell(x).
> $$
>
> *Uniqueness.* If $(x, a) = (x, a')$ for all $x \in H$, then $(x, a - a') = 0$ for all $x$; taking $x = a - a'$ gives $\|a - a'\|^2 = 0$, so $a = a'$. (Not written out in lecture.)

^pf-19-2-2

*Uses:* [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]], [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^pf-19-2|§19.2 (1)]], [[§18 Projection and Orthogonal Decomposition#^def-18-1|Def. §18.1]], [[§16 Definition and Examples#^def-16-1|Def. §16.1]]

![[m556-19-1.svg]]
*The kernel $N$, the line $N^\perp$, and the decomposition $x = kx_0 + y$ that locates $x$ on the level set $\{\ell = \ell(x)\}$.*

The null set $N$ is a closed hyperplane and $N^\perp$ a line; $a$ is a normal vector to $N$, a multiple of $x_0$. The level sets $\{\ell = c\}$ are the translates of $N$, and $\ell(x)$ records only which translate $x$ lies on, i.e. the $N^\perp$-component $kx_0$ of $x$.

> [!remark] Remark
> Wu on method: “when we try to prove a big theorem, very often the simple examples we learned, like in linear algebra, give the answer; start with simple examples and go from there.” Here the finite-dimensional picture dictated both the object to study ($\ker \ell$) and the candidate ($a$ normal to it); the analysis consisted of making the orthogonal decomposition available, which is where completeness of $H$ and boundedness of $\ell$ enter.

^rem-19-4

> [!remark] Remark: Comparison with Lax
> Lax proves the representation theorem through his Lemma 5: the null space of a nonzero functional has codimension one, and two functionals with the same null space are proportional. He takes $z \neq 0$ in $N^\perp$ and observes that $\ell$ and $x \mapsto (x, z)$ have the same null space, so $\ell$ is a multiple of $(\cdot, z)$. Wu's proof (Lemma [[§19 Bounded Linear Functionals and the Riesz Representation Theorem#^lem-19-4|§19.4]] and the explicit decomposition $x = kx_0 + y$) is the same argument with the proportionality constant computed by hand.

^rem-19-5
