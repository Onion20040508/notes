---
type: section
subject: "[[Functional Analysis]]"
chapter: 6
section: 35
tags: [functional-analysis, math556]
---
← [[§34 Weak Solutions of the Dirichlet Problem]] · ↑ [[· 6 Bounded Linear Maps]] · [[§36 ℝⁿ, Cᵐ and Lᵖ]] →

*Stage: maps — Thread: functionals. A density between two measures is the Riesz representer of a bounded functional on an $L^2$ space.*

Wu: the Radon–Nikodym theorem, whose measure-theoretic proof is difficult, follows quickly from the [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|Riesz representation theorem]]; it will be needed later. For those who have taken measure theory the definitions are a review.

> [!definition] Definition §35.1: $\sigma$-Algebra
> Let $X$ be a set. A collection $\mathcal{A}$ of subsets of $X$ is a **$\sigma$-algebra** if
> - (i) $\varnothing \in \mathcal{A}$;
> - (ii) if $A \in \mathcal{A}$, then $A^c = X \setminus A \in \mathcal{A}$;
> - (iii) if $A_j \in \mathcal{A}$ for $j = 1, 2, \ldots$, then $\bigcup_{j=1}^\infty A_j \in \mathcal{A}$.

^def-35-1

> [!remark]- Connections
> - Measure Theory home: [[§11 Lebesgue Measurable Sets#^def-11-4|551 Def. §11.4]] (an [[§11 Lebesgue Measurable Sets#^def-11-3|algebra]] closed under countable unions), with examples [[§11 Lebesgue Measurable Sets#^ex-11-2|551 Ex. §11.2]]; the Lebesgue measurable sets form one, [[Lebesgue Measurable Sets Form a σ-Algebra|551 §11.3]]; the Borel σ-algebra, [[§12 Borel Sets and Measure Spaces#^def-12-2|551 Def. §12.2]].

> [!definition] Definition §35.2: Measurable Space
> A **measurable space** is a pair $(X, \mathcal{A})$ of a set $X$ and a $\sigma$-algebra $\mathcal{A}$ of subsets of $X$ (Definition [[§35 Measures and the Radon–Nikodym Theorem#^def-35-1|§35.1]]).

^def-35-2

> [!remark]- Connections
> - Measure Theory home: [[§12 Borel Sets and Measure Spaces#^def-12-5|551 Def. §12.5]].

> [!definition] Definition §35.3: Measure
> A **(positive) measure** on a measurable space $(X, \mathcal{A})$ (Definition [[§35 Measures and the Radon–Nikodym Theorem#^def-35-2|§35.2]]) is a map $\mu : \mathcal{A} \to [0, \infty]$ with
> - (1) $\mu(\varnothing) = 0$;
> - (2) $\mu(A) \ge 0$ for all $A \in \mathcal{A}$;
> - (3) countable additivity: if $A_j \in \mathcal{A}$ are pairwise disjoint ($A_i \cap A_j = \varnothing$ for $i \neq j$), then $\mu\bigl( \bigcup_{j=1}^\infty A_j \bigr) = \sum_{j=1}^\infty \mu(A_j)$.

^def-35-3

> [!remark]- Connections
> - Measure Theory home: [[§12 Borel Sets and Measure Spaces#^def-12-6|551 Def. §12.6]] (same three axioms), measure space [[§12 Borel Sets and Measure Spaces#^def-12-7|551 Def. §12.7]]; counting and Dirac measures, [[§12 Borel Sets and Measure Spaces#^ex-12-2|551 Ex. §12.2]].

> [!definition] Definition §35.4: Finite Measure
> A measure $\mu$ on $(X, \mathcal{A})$ (Definition [[§35 Measures and the Radon–Nikodym Theorem#^def-35-3|§35.3]]) is **finite** if $\mu(X) < \infty$.

^def-35-4

> [!remark]- Connections
> - 551 has no separate definition; finiteness appears as $m(E) < \infty$, e.g. in the $L^p$ inclusion for finite measure [[§34 Normed Linear Spaces and Lᵖ Spaces#^cor-34-6|551 §34.6]], whose case $p_1 = 1$, $p_2 = 2$ is the bound in Step 1 of Theorem [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|§35.1]].

> [!example] Example §35.1: Lebesgue Measure and a Restriction of It
> On $\mathbb{R}^2$, [[§11 Lebesgue Measurable Sets#^def-11-5|Lebesgue measure]] $m$ gives a rectangle $R = [a,b] \times [c,d]$ the measure $m(R) = (b-a)(d-c)$; a general set is measured by [[§10 Lebesgue Outer Measure#^def-10-4|covering it with rectangles]]. On the same sets one can define other measures. Wu's example: fix a measurable set $\Omega$, “the piece of material we care about”, and let
>
> $$
> \nu(E) = m(E \cap \Omega) .
> $$
>
> A rectangle outside $\Omega$ has $\nu$-measure $0$, and one inside has $\nu(R) = m(R)$.

^ex-35-1

![[m556-35-1.svg]]
*Only the hatched part of $E$ counts for $\nu$; a set disjoint from $\Omega$ has $\nu$-measure zero, and a set of Lebesgue measure zero has $\nu$-measure zero.*

> [!definition] Definition §35.5: Absolute Continuity
> Let $\mu$ and $\nu$ be measures on the same measurable space $(X, \mathcal{A})$. $\nu$ is **absolutely continuous** with respect to $\mu$, written $\nu \ll \mu$, if
>
> $$
> \mu(E) = 0 \implies \nu(E) = 0 \qquad \text{for all } E \in \mathcal{A} .
> $$

^def-35-5

> [!remark]- Connections
> - 551 defines absolute continuity only for functions, [[§31 Absolute Continuity#^def-31-1|551 Def. §31.1]]. For a measure with an integrable density, $\nu(E) = \int_E |f|$, the $\varepsilon$–$\delta$ form “$m(E) < \delta \Rightarrow \nu(E) < \varepsilon$” is the [[§24 The L¹ Space and Density Theorems#^thm-24-2|absolute continuity of the integral, 551 §24.2]].

> [!example] Example §35.2: The Restricted Measure has a Density
> In Example [[§35 Measures and the Radon–Nikodym Theorem#^ex-35-1|§35.1]], $\nu \ll m$: if $m(E) = 0$ then $0 \le \nu(E) = m(E \cap \Omega) \le m(E) = 0$. Moreover $\nu(E) = \int_E \chi_\Omega\, dm$. The [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|theorem below]] says that this is the general situation: a measure absolutely continuous with respect to $\mu$ is $\mu$ weighted by a density.

^ex-35-2

> [!remark]- Connections
> - $\nu$ is the measure induced by the non-negative function $\chi_\Omega$: [[§21 Consequences of the Monotone Convergence Theorem#^def-21-1|551 Def. §21.1]].

> [!remark] Remark: Facts Assumed from Measure Theory
> Integration against an abstract measure is assumed as in a course on measure theory: for a measure $\lambda$, $L^2(\lambda)$ (real functions with $\int f^2 d\lambda < \infty$, identified when equal $\lambda$-a.e.) is a [[§23 Cauchy–Schwarz and the Induced Norm#^def-23-1|Hilbert space]] with $(f, g) = \int f g\, d\lambda$; the [[Monotone Convergence Theorem (Lebesgue)|monotone convergence theorem]]; and [[Continuity of Measure|continuity of measure from below]]. If $\mu, \nu$ are measures, so is $\mu + \nu$ (sums of non-negative series can be rearranged), and $\int h\, d(\mu+\nu) = \int h\, d\mu + \int h\, d\nu$ for every measurable $h \ge 0$, hence for every $h \in L^1(\mu + \nu)$.

^rem-35-1

> [!remark]- Connections
> - 551 proves these for Lebesgue measure on $\mathbb{R}^n$: $L^p$ spaces [[§34 Normed Linear Spaces and Lᵖ Spaces#^def-34-6|551 Def. §34.6]] and their completeness, the [[Riesz–Fischer Theorem|Riesz–Fischer theorem]] ([[§35 Lᵖ as a Banach Space#^thm-35-11|551 §35.11]]); the monotone convergence theorem [[§20 The Lebesgue Integral for Simple Functions#^thm-20-7|551 §20.7]]; continuity from below [[§13 Approximation and Continuity of Measure#^prop-13-4|551 §13.4]]. The course's own $L^2(\Omega)$: [[§22 Definition and Examples#^ex-22-3|Ex. §22.3]].

> [!theorem] Theorem §35.1: Radon–Nikodym
> Let $(X, \mathcal{A})$ be a measurable space and $\mu, \nu$ finite measures on it with $\nu \ll \mu$. Then there is a measurable $g \ge 0$ with $g \in L^1(\mu)$ (i.e. $\int_X g\, d\mu < \infty$) such that
>
> $$
> \nu(E) = \int_E g(x)\, d\mu(x) \qquad \text{for all } E \in \mathcal{A} .
> $$

^thm-35-1

> [!proof]+ Proof
> (von Neumann's proof, following Wu; real scalars throughout.)
>
> **Step 1: the Hilbert space and the functional.** Let $H = L^2(\mu + \nu)$, with $(f, g) = \int_X f g\, d(\mu + \nu)$, and $\ell(f) = \int_X f\, d\mu$ for $f \in H$. $\ell$ is linear. It is [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|bounded]]: by [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Cauchy–Schwarz]] in $L^2(\mu)$ and $\mu \le \mu + \nu$,
>
> $$
> |\ell(f)| \le \Bigl( \int_X f^2\, d\mu \Bigr)^{1/2} \Bigl( \int_X 1\, d\mu \Bigr)^{1/2} \le \mu(X)^{1/2} \Bigl( \int_X f^2\, d(\mu + \nu) \Bigr)^{1/2} = \mu(X)^{1/2}\, \|f\|_H .
> $$
>
> (If $f = 0$ $(\mu+\nu)$-a.e. then $f = 0$ $\mu$-a.e., so $\ell$ is defined on classes, and the inequality shows $f \in L^1(\mu)$.)
>
> **Step 2: Riesz.** By Theorem [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|§26.4]] there is a unique $g_0 \in H$ with
>
> $$
> \int_X f\, d\mu = \ell(f) = (f, g_0) = \int_X f g_0\, d(\mu + \nu) \qquad \text{for all } f \in H .
> $$
>
> Since $f g_0 \in L^1(\mu + \nu)$ (Cauchy–Schwarz in $H$), the last integral splits as $\int f g_0\, d\mu + \int f g_0\, d\nu$, and rearranging,
>
> $$
> \int_X f\, (1 - g_0)\, d\mu = \int_X f g_0\, d\nu \qquad \text{for all } f \in H . \tag{$\ast$}
> $$
>
> **Step 3: $0 < g_0 \le 1$ $\mu$-a.e.** Fix a real-valued measurable representative of $g_0$. Let $F_1 = \{ x : g_0(x) \le 0 \}$ and take $f = \chi_{F_1}$, which is in $H$ since $\mu + \nu$ is finite. On $F_1$, $1 - g_0 \ge 1$ and $g_0 \le 0$, so by ($\ast$)
>
> $$
> \mu(F_1) = \int_X \chi_{F_1}\, d\mu \le \int_X \chi_{F_1} (1 - g_0)\, d\mu = \int_X \chi_{F_1}\, g_0\, d\nu \le 0 .
> $$
>
> Hence $\mu(F_1) = 0$. Next let $F_2 = \{ x : g_0(x) > 1 \}$ and take $f = \chi_{F_2}$. Then
>
> $$
> \int_X \chi_{F_2}(1 - g_0)\, d\mu = \int_X \chi_{F_2}\, g_0\, d\nu \ge \nu(F_2) \ge 0 .
> $$
>
> If $\mu(F_2) > 0$, the left side is $< 0$, since $1 - g_0 < 0$ on $F_2$ — a contradiction. (Strictly: $F_2 = \bigcup_k \{ g_0 > 1 + \frac1k \}$, so some $G_k = \{ g_0 > 1 + \frac1k\}$ has $\mu(G_k) > 0$, and the left side is at most $-\frac1k \mu(G_k) < 0$.) Hence $\mu(F_2) = 0$.
>
> **Step 4: modify $g_0$ on a null set.** By [[§35 Measures and the Radon–Nikodym Theorem#^def-35-5|absolute continuity]], $\nu(F_1 \cup F_2) = 0$ as well; this is where $\nu \ll \mu$ is used. Redefine $g_0 = 1$ on $F_1 \cup F_2$. The new $g_0$ differs from the old one only on a set of $(\mu + \nu)$-measure zero, so it is the same element of $H$ and ($\ast$) still holds; now $0 < g_0(x) \le 1$ for every $x \in X$.
>
> **Step 5: the density.** Define
>
> $$
> g(x) = \frac{1 - g_0(x)}{g_0(x)} \ge 0,
> $$
>
> measurable as a quotient of measurable functions with a denominator that never vanishes. Wu's choice of test function is $f = \chi_E / g_0$ for $E \in \mathcal{A}$: then $f g_0 = \chi_E$ and $f(1 - g_0) = \chi_E\, g$, so ($\ast$) reads $\int_E g\, d\mu = \nu(E)$. Wu left one check to the class: $f \in H$.
> This needs care, because $g_0$ may take arbitrarily small values, and then $\chi_E/g_0$ need not be in $L^2(\mu + \nu)$. Truncate: for $k \in \mathbb{N}$ let $E_k = E \cap \{ g_0 \ge \frac1k \}$ and $f_k = \chi_{E_k}/g_0$. Then $0 \le f_k \le k$, so $f_k \in H$, and ($\ast$) with $f = f_k$ gives
>
> $$
> \nu(E_k) = \int_X \chi_{E_k}\, d\nu = \int_X f_k g_0\, d\nu = \int_X f_k (1 - g_0)\, d\mu = \int_{E_k} g\, d\mu .
> $$
>
> Since $g_0 > 0$ everywhere, the sets $E_k$ increase to $E$. By [[Continuity of Measure|continuity of measure from below]], $\nu(E_k) \to \nu(E)$; by the [[Monotone Convergence Theorem (Lebesgue)|monotone convergence theorem]] ($0 \le g\chi_{E_k} \uparrow g\chi_E$), $\int_{E_k} g\, d\mu \to \int_E g\, d\mu$. Hence $\nu(E) = \int_E g\, d\mu$.
>
> **Step 6: integrability.** Taking $E = X$, $\int_X g\, d\mu = \nu(X) < \infty$, so $g \in L^1(\mu)$.

^pf-35-1

*Uses:* [[§35 Measures and the Radon–Nikodym Theorem#^def-35-4|Def. §35.4]], [[§35 Measures and the Radon–Nikodym Theorem#^def-35-5|Def. §35.5]], [[§35 Measures and the Radon–Nikodym Theorem#^rem-35-1|Remark §35 (facts assumed)]], [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|§23.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Def. §26.1]], [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|§26.4]], [[§13 Approximation and Continuity of Measure#^prop-13-4|551 §13.4]], [[§20 The Lebesgue Integral for Simple Functions#^thm-20-7|551 §20.7]]

> [!remark]- Connections
> - The converse direction: every non-negative measurable density defines a measure, [[§21 Consequences of the Monotone Convergence Theorem#^def-21-1|551 Def. §21.1]], and that measure is absolutely continuous with respect to Lebesgue measure (its integral over a null set vanishes, [[§21 Consequences of the Monotone Convergence Theorem#^prop-21-2|551 §21.2]]).
> - The proof is one more application of the [[Riesz Representation Theorem (Hilbert spaces)|Riesz representation theorem]], here on $L^2(\mu + \nu)$.

> [!definition] Definition §35.6: Radon–Nikodym Derivative
> A function $g$ as in Theorem [[§35 Measures and the Radon–Nikodym Theorem#^thm-35-1|§35.1]] is a **Radon–Nikodym derivative** of $\nu$ with respect to $\mu$, written $g = \dfrac{d\nu}{d\mu}$; the theorem reads $\nu(E) = \int_E \frac{d\nu}{d\mu}\, d\mu$.

^def-35-6

> [!remark] Remark: Where Absolute Continuity is Used
> A student asked where $\nu \ll \mu$ enters; Wu: “not yet” through Step 3, and then in Step 4. It is needed only for $F_1$. For $F_2$ it is automatic: ($\ast$) with $f = \chi_{F_2}$ and $\mu(F_2) = 0$ gives $\int_{F_2} g_0\, d\nu = 0$ with $g_0 > 1$ on $F_2$, so $\nu(F_2) = 0$. But $\nu(F_1) = 0$ can fail without absolute continuity. Example: $X = [0,1]$, $\mu$ Lebesgue measure, $\nu = \delta_0$ the [[§12 Borel Sets and Measure Spaces#^ex-12-2|unit point mass]] at $0$. Then ($\ast$) forces $g_0 = 1$ $\mu$-a.e. and $g_0(0) = 0$, so $F_1 = \{0\}$ has $\mu(F_1) = 0$ but $\nu(F_1) = 1$: the point mass hides exactly where $g_0 = 0$, and no density exists.

^rem-35-2

> [!remark] Remark
> The truncation in Step 5 is necessary, not cosmetic. On $X = [0,1]$ with $\mu$ Lebesgue measure and $d\nu = x^{-1/2}\, dx$ (a finite measure, $\nu \ll \mu$), the proof produces $g_0 = 1/(1 + x^{-1/2})$, and $\chi_X / g_0 = 1 + x^{-1/2}$ has $\int (1 + x^{-1/2})^2\, d(\mu + \nu) = \int_0^1 (1 + x^{-1/2})^3\, dx = \infty$. Here $d\nu/d\mu = x^{-1/2}$ (Definition [[§35 Measures and the Radon–Nikodym Theorem#^def-35-6|§35.6]]). The density is unique $\mu$-a.e., and the theorem also holds for $\sigma$-finite and for signed measures (Wu: “Radon–Nikodym has a more general statement”). Neither was covered.

^rem-35-3

> [!remark]- Connections
> - The power singularities behind the example ($\int_0^1 x^{-a}\,dx < \infty$ iff $a < 1$): [[Power singularities 1∕xᵃ]]; $1/\sqrt{x} \in L^1 \setminus L^2$ on $(0,1)$, [[§34 Normed Linear Spaces and Lᵖ Spaces#^ex-34-5|551 Ex. §34.5]].
