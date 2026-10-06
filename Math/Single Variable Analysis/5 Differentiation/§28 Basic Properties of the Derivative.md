---
type: section
subject: "[[Single Variable Analysis]]"
section: 28
chapter: 5
tags: [real-analysis, math451]
---
← [[§27 Weierstrass's Approximation Theorem (Not Covered)]] · ↑ [[· 5 Differentiation]] · [[§29 The Mean Value Theorem]] →

> [!definition] Definition §28.1: The Derivative
> Let $I = (\alpha, \beta)$ be an open interval, $f: I \to \mathbb{R}$, and $a \in I$. We say $f$ is **differentiable at $a$** if
>
> $$
> \lim_{x \to a} \frac{f(x) - f(a)}{x - a}
> $$
>
> exists and is *finite*; the limit is denoted $f'(a)$. Note: in this limit $x \to a$ with $x \neq a$ (the difference quotient is undefined at $x = a$) — this is exactly the punctured-interval limit of §20. If the limit does not exist (or is infinite), $f$ is not differentiable at $a$.

^def-28-1

![[m451-28-2.svg]]
*The derivative as a limit of secant slopes: as $x \to a$, the secants (blue, lighter to darker) through $(a, f(a))$ and $(x, f(x))$ pivot into the tangent line (red), whose slope is $f'(a)$. Only $x \neq a$ is ever used — at $x = a$ there is no secant.*

> [!remark]- Connections
> - In several variables it splits into partial derivatives, [[§4 Partial Derivatives#^def-4-1|452 Def. §4.1]], directional derivatives, [[§7 Directional Derivatives#^def-7-1|452 Def. §7.1]], and differentiability as linear approximation, [[§6 Differentiability#^def-6-1|452 Def. §6.1]].
> - Computational version: [[§12 Derivatives and Rates of Change#^def-12-3|Calc Def. §12.3]], [[§13 The Derivative as a Function#^def-13-3|Calc Def. §13.3]] (with worked examples).
> - Computational version: [[§19 Derivatives#^def-19-1|342 Def. §19.1]] (the complex derivative, the same difference quotient with z in place of x, with worked examples).

> [!example] Example §28.1: Square Root of the Absolute Value
> Show $f(x) = \sqrt{|x|}: \mathbb{R} \to \mathbb{R}$ is differentiable at every $a \neq 0$ but not at $a = 0$.
>
> **Case $a > 0$** (the case $a < 0$ is similar). Near $a$, $f(x) = \sqrt x$; by the conjugate,
>
> $$
> \frac{\sqrt x - \sqrt a}{x - a} = \frac{1}{\sqrt x + \sqrt a} \longrightarrow \frac{1}{2\sqrt a},
> $$
>
> using the continuity of $\sqrt{\ }$ (§17). So $f$ is differentiable at $a$ with $f'(a) = \tfrac{1}{2\sqrt a}$.
>
> **Case $a = 0$.** The argument above fails (division by $\sqrt a = 0$); in fact,
>
> $$
> x > 0: \quad \frac{\sqrt x - 0}{x - 0} = \frac{1}{\sqrt x} \longrightarrow +\infty; \qquad
> x < 0: \quad \frac{\sqrt{|x|}}{x} = -\frac{1}{\sqrt{|x|}} \longrightarrow -\infty.
> $$
>
> No finite limit — $\sqrt{|x|}$ is not differentiable at $0$.

^ex-28-1

> [!example] Example §28.2: The Power Function
> Show $f(x) = x^n$ is differentiable with $f'(x) = n x^{n-1}$. We all know the formula — but how to *find* it? Factor:
>
> $$
> x^n - a^n = (x - a)\left( x^{n-1} + a x^{n-2} + a^2 x^{n-3} + \cdots + a^{n-2} x + a^{n-1} \right),
> $$
>
> so
>
> $$
> \frac{f(x) - f(a)}{x - a} = x^{n-1} + a x^{n-2} + \cdots + a^{n-1} \longrightarrow \underbrace{a^{n-1} + \cdots + a^{n-1}}_{n \text{ terms}} = n a^{n-1},
> $$
>
> by continuity of polynomials. Hence $(x^n)' = n x^{n-1}$.

^ex-28-2

> [!remark]- Connections
> - Computational version: the Power Rule, [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|Calc Thm. §14.2]] (with worked examples).

> [!theorem] Theorem §28.1: Differentiable Implies Continuous
> If $f$ is differentiable at $a$, then $f$ is continuous at $a$.

^thm-28-1

> [!proof]+ Proof
> We must show $\lim_{x\to a} f(x) = f(a)$, i.e. $f(x) - f(a) \to 0$. Write
>
> $$
> f(x) - f(a) = \frac{f(x) - f(a)}{x - a} \cdot (x - a) \longrightarrow f'(a) \cdot 0 = 0,
> $$
>
> by the product rule for limits of functions. Done.

^pf-28-1

*Uses:* [[§20 Limits of Functions#^rem-20-2|§20 Rem. (limit laws)]]

> [!remark]- Connections
> - Computational version: [[§13 The Derivative as a Function#^thm-13-1|Calc Thm. §13.1]].
> - Computational version: [[§19 Derivatives#^thm-19-1|342 Thm. §19.1]] (the same statement and proof for complex functions).

> [!remark] Remark: The Converse Fails
> Two counterexamples: $\sqrt{|x|}$ (continuous everywhere, not differentiable at $0$, as above — the difference quotients blow up); and $|x|$, where the one-sided limits of $\tfrac{f(x) - f(0)}{x - 0} = \tfrac{|x|}{x}$ are $+1$ and $-1$ and disagree. Using $|x|$, one can build continuous functions non-differentiable at finitely many prescribed points, e.g.
>
> $$
> |x+1| + |x| + |x-1|
> $$
>
> fails differentiability exactly at $-1, 0, 1$ (near each of these points, two of the three summands are differentiable and one is not; a sum of a differentiable and a non-differentiable function is non-differentiable). Can one construct a *continuous function differentiable at no point*? Yes — Weierstrass did — but it is a long story.

^rem-28-1

![[m451-28-3.svg]]
*Continuous but not differentiable. Left: the secant slopes of $\sqrt{|x|}$ at $0$ (red, through $x = \pm 0.4$ and $x = \pm 0.1$) are $\pm\tfrac{1}{\sqrt{|x|}}$ and blow up to $\pm\infty$ — a cusp. Right: $|x+1| + |x| + |x-1|$ is piecewise linear with slopes $-3, -1, 1, 3$; at each corner $-1, 0, 1$ (red) the two one-sided slopes disagree.*

> [!remark]- Connections
> - Worked examples: $|x|$ at $0$, [[§13 The Derivative as a Function#^ex-13-4|Calc Ex. §13.4]].

> [!theorem] Theorem §28.2: Arithmetic of Derivatives
> If $f, g$ are differentiable at $a$, then $f \pm g$ and $fg$ are differentiable at $a$, with
>
> $$
> (f \pm g)'(a) = f'(a) \pm g'(a), \qquad (fg)'(a) = f'(a) g(a) + f(a) g'(a);
> $$
>
> and if $g(a) \neq 0$, then $f/g$ is differentiable at $a$, with the usual quotient rule.

^thm-28-2

> [!proof]+ Proof
> The sum rule follows directly from the limit theorems. For the **product**, insert the mixed term $f(a)g(x)$:
>
> $$
> \frac{f(x)g(x) - f(a)g(a)}{x-a}
> = \frac{f(x) - f(a)}{x-a}\, g(x) + f(a)\, \frac{g(x) - g(a)}{x-a}
> \longrightarrow f'(a) g(a) + f(a) g'(a),
> $$
>
> where in the first summand we used the *continuity* of $g$ at $a$ (which follows from its differentiability — the theorem above). The quotient rule is proved similarly (or by combining the product rule with the derivative of $1/g$).

^pf-28-2

*Uses:* [[§20 Limits of Functions#^rem-20-2|§20 Rem. (limit laws)]], [[§28 Basic Properties of the Derivative#^thm-28-1|§28.1]]

> [!remark]- Connections
> - Two-variable versions for partial derivatives and for differentiability: [[§6 Differentiability#^thm-6-3|452 Thm. §6.3]] to [[§6 Differentiability#^thm-6-5|452 Thm. §6.5]], and [[§6 Differentiability#^thm-6-6|452 Thm. §6.6]] to [[§6 Differentiability#^thm-6-8|452 Thm. §6.8]].
> - Computational version: [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-4|Calc Thm. §14.4]], [[§15 The Product and Quotient Rules#^thm-15-1|Calc Thm. §15.1]], [[§15 The Product and Quotient Rules#^thm-15-2|Calc Thm. §15.2]] (with worked examples).
> - Computational version: [[§20 Rules for Differentiation#^thm-20-2|342 Thm. §20.2]] (sum, product and quotient rules for complex derivatives, with worked examples).

## The Chain Rule and a Gap

The most useful theorem:

> [!theorem] Theorem §28.3: Chain Rule
> If $f$ is differentiable at $a$ and $g$ is differentiable at $f(a)$, then $g(f(x))$ is differentiable at $a$, and
>
> $$
> \bigl( g(f(x)) \bigr)'\big|_{x=a} = g'(f(a))\, f'(a).
> $$

^thm-28-3

> [!proof]+ Proof (first attempt)
> Multiply and divide by $f(x) - f(a)$:
>
> $$
> \frac{g(f(x)) - g(f(a))}{x - a} = \frac{g(f(x)) - g(f(a))}{f(x) - f(a)} \cdot \frac{f(x) - f(a)}{x - a}.
> $$
>
> Since $f$ is continuous at $a$, $f(x) \to f(a)$, so the first factor tends to $g'(f(a))$ (differentiability of $g$ at $f(a)$, along the values $f(x) \to f(a)$), and the second tends to $f'(a)$; the product tends to $g'(f(a)) f'(a)$.
>
> **Is this a good proof? Any problem?** Yes, there is one: in the limit defining $g'$, the increment must be *nonzero* — but here it can happen that $f(x) = f(a)$ for $x \neq a$ arbitrarily close to $a$ (e.g. for constant $f$, or $f(x) = x^2\sin\tfrac1x$ at $a = 0$), and then the first factor is $\tfrac00$: undefined. The proof is valid whenever $f(x) \neq f(a)$ near $a$; the general case needs a repair.

^pf-28-3

*Uses:* [[§28 Basic Properties of the Derivative#^thm-28-1|§28.1]]

> [!proof]+ Proof (repaired)
> The trick: take care of the case $f(x) = f(a)$ by never using $f(x) - f(a)$ as a denominator. Define a new function $h$ on the domain of $g$:
>
> $$
> h(y) =
> \begin{cases}
> \ \dfrac{g(y) - g(f(a))}{y - f(a)} & y \neq f(a), \\[2mm]
> \ g'(f(a)) & y = f(a).
> \end{cases}
> $$
>
> *Claim: $h$ is continuous at $f(a)$.* Why? Because $\lim_{y \to f(a)} \tfrac{g(y)-g(f(a))}{y - f(a)} = g'(f(a))$ is exactly the definition of the derivative of $g$ at $f(a)$ — so the limit of $h$ at $f(a)$ equals its assigned value there (§20).
>
> Next, the key identity: for *all* $y$ in the domain of $g$,
>
> $$
> g(y) - g(f(a)) = h(y)\,\bigl(y - f(a)\bigr).
> $$
>
> Check the two cases: for $y \neq f(a)$ this is the definition of $h$; for $y = f(a)$ both sides are $0$.
>
> Now substitute $y = f(x)$ — valid for every $x$, no case distinction needed:
>
> $$
> \frac{g(f(x)) - g(f(a))}{x - a} = h(f(x)) \cdot \frac{f(x) - f(a)}{x - a}.
> $$
>
> As $x \to a$: $f(x) \to f(a)$ ($f$ continuous at $a$), and $h$ is continuous at $f(a)$, so $h(f(x)) \to h(f(a)) = g'(f(a))$; and the second factor tends to $f'(a)$. Hence the limit exists and equals $g'(f(a))\, f'(a)$. Done!

^pf-28-3-2

*Uses:* [[§28 Basic Properties of the Derivative#^thm-28-1|§28.1]], [[§20 Limits of Functions#^thm-20-1|§20.1]], [[§17 Continuous Functions#^thm-17-4|§17.4]]

> [!remark]- Connections
> - Computational version: [[§20 Rules for Differentiation#^thm-20-4|342 Thm. §20.4]] (the complex chain rule, with the same repair of the naive proof).

> [!remark] Remark: The Classical Notation
> If $y = y(x)$ and $z = z(y)$, then $z = z(y(x))$ is a function of $x$, and the chain rule reads
>
> $$
> \frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx},
> $$
>
> where $dz, dy, dx$ are *differentials* — historically viewed as infinitely small but *nonzero* quantities, which is why $dy$ could sit in a denominator. The gap in the naive proof above is precisely the modern price of that old picture: $\Delta y = f(x) - f(a)$, unlike the ideal $dy$, can actually vanish.

^rem-28-2

> [!remark]- Connections
> - Several-variable chain rule: [[§6 Differentiability#^thm-6-9|452 Thm. §6.9]] (for differentiable maps) and [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]] (with continuous partials).
> - Computational version: [[§17 The Chain Rule#^thm-17-2|Calc Thm. §17.2]] (with worked examples).

> [!example] Example §28.3: Oscillation and Differentiability at Zero
> **(1)** $f(x) = x \sin\tfrac1x$ ($x \neq 0$), $f(0) = 0$: continuous at $0$ (proved in §17) but *not differentiable* at $0$ — the difference quotient
>
> $$
> \frac{f(x) - f(0)}{x - 0} = \sin\frac1x
> $$
>
> has no limit as $x \to 0$ (the oscillation argument of §17).
>
> **(2)** $g(x) = x^3 \sin\tfrac1x$ ($x \neq 0$), $g(0) = 0$: differentiable at *every* $a \in \mathbb{R}$. At $a = 0$:
>
> $$
> \frac{g(x) - g(0)}{x - 0} = x^2 \sin\frac1x \longrightarrow 0
> $$
>
> (null times bounded), so $g'(0) = 0$. At $a \neq 0$, combine the product rule and the chain rule ($\sin$ and $\tfrac1x$ differentiable away from $0$, on the usual credit for $\sin$).

^ex-28-3

> [!example] Example §28.4: The Middle Rung (HW)
> Between the two lies $h(x) = x^2 \sin\tfrac1x$ ($x \neq 0$), $h(0) = 0$: *differentiable everywhere — but $h'$ is not continuous*. At $0$, as for $g$ above,
>
> $$
> \frac{h(x) - h(0)}{x - 0} = x \sin\frac1x \longrightarrow 0 \qquad \text{(null times bounded)},
> $$
>
> so $h'(0) = 0$. Away from $0$, product and chain rules give
>
> $$
> h'(x) = 2x \sin\frac1x - \cos\frac1x \qquad (x \neq 0).
> $$
>
> As $x \to 0$ the first term tends to $0$, but $\cos\tfrac1x$ has no limit: along $x_n = \tfrac{1}{n\pi} \to 0$, $\cos\tfrac{1}{x_n} = \cos(n\pi) = (-1)^n$ oscillates. So $\lim_{x\to0} h'(x)$ does not exist, and in particular does not equal $h'(0) = 0$: $h'$ is discontinuous at $0$.
>
> The three examples form a ladder governed by the power of $x$ damping the oscillation: $x\sin\tfrac1x$ is continuous but not differentiable at $0$; $x^2\sin\tfrac1x$ is differentiable but not $C^1$; $x^3\sin\tfrac1x$ is $C^1$ (its derivative $3x^2\sin\tfrac1x - x\cos\tfrac1x \to 0 = g'(0)$, both terms null times bounded). Each extra power buys exactly one more degree of regularity at the origin. This $h$ is the “standard example” promised in §29's Darboux discussion: a derivative that exists everywhere yet is discontinuous — the reason Darboux's theorem cannot be reduced to the [[Intermediate Value Theorem|IVT]].

^ex-28-4

![[m451-28-1.svg]]
*The oscillation ladder with its envelopes (dashed): $x \sin\tfrac1x$ hugs $\pm x$ — continuous at $0$, not differentiable; $x^2 \sin\tfrac1x$ hugs $\pm x^2$ — differentiable, but $f'$ oscillates without limit. Each extra power of damping flattens the envelope by one order at the origin.*

Computations with piecewise functions — the corner examples above — all follow one pattern. It deserves a statement:

> [!theorem] Proposition §28.4: Differentiability of a Piecewise Function (HW)
> Let $f, g$ be differentiable on an open interval $I$, let $a \in I$, and define
>
> $$
> h(x) = \begin{cases} f(x), & x < a, \\ g(x), & x \geq a. \end{cases}
> $$
>
> Then $h$ is differentiable at $a$ if and only if *both*
>
> $$
> f(a) = g(a) \qquad \text{and} \qquad f'(a) = g'(a)
> $$
>
> hold — the two branches must agree in *value* and in *slope* — and in that case $h'(a)$ is the common value $f'(a) = g'(a)$.

^prop-28-4

> [!proof]+ Proof
> Note $h(a) = g(a)$ by definition.
>
> ($\Rightarrow$) If $h$ is differentiable at $a$, it is continuous there; the left limit is $\lim_{x \to a^-} f(x) = f(a)$ ($f$ continuous, being differentiable), and it must equal $h(a) = g(a)$: value match. Then the two one-sided difference quotients of $h$,
>
> $$
> \lim_{x \to a^-} \frac{f(x) - f(a)}{x - a} = f'(a), \qquad
> \lim_{x \to a^+} \frac{g(x) - g(a)}{x - a} = g'(a)
> $$
>
> (using $h(a) = f(a) = g(a)$ on the left), both exist and must equal the two-sided limit $h'(a)$: slope match.
>
> ($\Leftarrow$) With $f(a) = g(a)$, the same two computations show the one-sided limits of $\tfrac{h(x)-h(a)}{x-a}$ are $f'(a)$ and $g'(a)$; if these agree, the two-sided limit exists and $h'(a) = f'(a) = g'(a)$.

^pf-28-4

*Uses:* [[§28 Basic Properties of the Derivative#^thm-28-1|§28.1]], [[§20 Limits of Functions#^thm-20-2|§20.2]]

> [!remark] Remark
> Read backwards, this organizes every corner in this section: $|x|$ glues $-x$ and $x$ at $0$ with matching values ($0 = 0$) but slopes $-1 \neq 1$ — corner; more generally, $|u|$ has a corner at every point where $u$ crosses $0$ with $u' \neq 0$ (slopes $\pm u'$), while at a zero of $u$ with $u' = 0$ the glue is smooth. Read forwards, it is the design rule for splines: to join two formulas differentiably, match value and slope at the seam.

^rem-28-3
