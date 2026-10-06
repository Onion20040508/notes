---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 34
stewart: "4.7"
aliases: ["Stewart 4.7"]
tags: [calculus]
---
← [[§33 Graphing with Calculus and Technology]] · ↑ [[· 4 Applications of Differentiation]] · [[§35 Newton's Method]] →

*Stewart, Section 4.7.*

The methods of [[§28 Maximum and Minimum Values|§28]] and [[§30 What Derivatives Tell Us About the Shape of a Graph|§30]] for finding extreme values apply to practical problems: maximize an area, a volume or a profit, minimize a distance, a time or a cost. The main difficulty is usually not the calculus but turning the words into a function of one variable on a definite domain. Once that is done, the Closed Interval Method handles closed intervals, and a new variant of the First Derivative Test handles open or infinite intervals, where there are no endpoints to compare. Problems with several variables and constraints come back in [[§113 Maximum and Minimum Values|§113]] and [[§114 Lagrange Multipliers|§114]].

> [!remark] Remark: Method — Steps in Solving Optimization Problems
> 1. **Understand the problem.** Read it until it is clearly understood. What is the unknown? What are the given quantities? What are the given conditions?
> 2. **Draw a diagram.** In most problems it helps to draw one and mark the given and required quantities on it.
> 3. **Introduce notation.** Assign a symbol to the quantity to be maximized or minimized (call it $Q$ for now), and symbols ($a, b, c, \ldots, x, y$) for the other unknown quantities. Suggestive initials help: $A$ for area, $h$ for height, $t$ for time.
> 4. **Express $Q$** in terms of some of the other symbols from Step 3.
> 5. **Reduce to one variable.** If $Q$ depends on more than one variable, use the given information to find equations relating them, and use these to eliminate all but one variable, so that $Q = f(x)$. Write the **domain** of $f$ in the given context.
> 6. **Find the absolute maximum or minimum** of $f$ with the methods of Sections 4.1 and 4.3. If the domain is a closed interval, the [[§28 Maximum and Minimum Values#^rem-28-2|Closed Interval Method]] can be used; otherwise use the First Derivative Test for Absolute Extreme Values ([[§34 Optimization Problems#^thm-34-1|Theorem §34.1]] below).
>
> The choice of variable in Step 5 matters: a well-chosen variable (an angle, say) can make Step 6 much easier.

^rem-34-1

> [!example] Example §34.1: Fencing a Field Along a River
> A farmer has $2400$ ft of fencing and wants to fence off a rectangular field that borders a straight river. He needs no fence along the river. What are the dimensions of the field that has the largest area?
>
> **Experiment.** A shallow, wide field ($100 \times 2200$) has area $220{,}000$ ft²; a deep, narrow one ($1000 \times 400$) has $400{,}000$ ft²; $700 \times 1000$ gives $700{,}000$ ft². Some intermediate shape seems best.
>
> **Set up.** Let $x$ be the depth and $y$ the width of the rectangle (in feet), so that the fence consists of two sides of length $x$ and one of length $y$. The area is $A = xy$. All the fencing is used, so $2x + y = 2400$, hence $y = 2400 - 2x$ and
>
> $$
> A = x(2400 - 2x) = 2400x - 2x^2 .
> $$
>
> Since $x \ge 0$ and $y \ge 0$ (that is, $x \le 1200$), the function to maximize is
>
> $$
> A(x) = 2400x - 2x^2, \qquad 0 \le x \le 1200 .
> $$
>
> **Solve.** $A'(x) = 2400 - 4x = 0$ gives $x = 600$. By the Closed Interval Method, compare $A(0) = 0$, $A(600) = 1{,}440{,}000 - 720{,}000 = 720{,}000$ and $A(1200) = 0$: the maximum value is $A(600) = 720{,}000$. (Alternatively, $A''(x) = -4 < 0$ for all $x$, so $A$ is concave downward everywhere and the local maximum at $600$ must be the absolute maximum.)
>
> The width is $y = 2400 - 2(600) = 1200$. So the field should be $600$ ft deep and $1200$ ft wide.
>
> *Stewart: Example 4.7.1*

^ex-34-1

When the domain is not a closed interval there are no endpoints to compare, and the Closed Interval Method does not apply. The following variant of the First Derivative Test ([[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-2|Theorem §30.2]]), which concerns only *local* extrema, takes its place.

> [!theorem] Theorem §34.1: First Derivative Test for Absolute Extreme Values
> Suppose that $c$ is a critical number of a continuous function $f$ defined on an interval.
>
> (a) If $f'(x) > 0$ for all $x < c$ and $f'(x) < 0$ for all $x > c$, then $f(c)$ is the absolute maximum value of $f$.
>
> (b) If $f'(x) < 0$ for all $x < c$ and $f'(x) > 0$ for all $x > c$, then $f(c)$ is the absolute minimum value of $f$.
>
> (Here $x$ ranges over the interval.)
>
> *Stewart: 4.7, Note 1 (First Derivative Test for Absolute Extreme Values)*

^thm-34-1

> [!proof]+ Proof
> Stewart justifies it in [[§34 Optimization Problems#^ex-34-2|Example §34.2]] below: $f$ is decreasing for *all* $x$ to the left of $c$ and increasing for *all* $x$ to the right. In detail:
>
> (a) Let $x < c$ be in the interval. $f$ is continuous on $[x, c]$ and differentiable on $(x, c)$, so the Mean Value Theorem gives $\xi \in (x, c)$ with $f(c) - f(x) = f'(\xi)(c - x) > 0$; thus $f(x) < f(c)$. Let $x > c$ be in the interval. Then $f(x) - f(c) = f'(\xi)(x - c)$ for some $\xi \in (c, x)$, and $f'(\xi) < 0$, so $f(x) < f(c)$. Hence $f(c) \ge f(x)$ for every $x$ in the interval: $f(c)$ is the absolute maximum value.
>
> (b) The same argument with the signs reversed gives $f(x) > f(c)$ for all $x \ne c$ in the interval.

^pf-34-1

*Uses:* [[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-2|§29.2]], [[§28 Maximum and Minimum Values#^def-28-1|Def. §28.1]]

> [!example] Example §34.2: The Cheapest Can
> A cylindrical can is to be made to hold $1$ L of oil. Find the dimensions that will minimize the cost of the metal to manufacture the can.
>
> **Set up.** Let $r$ be the radius and $h$ the height, in centimeters. To minimize the cost of the metal we minimize the total surface area: top and bottom are disks of area $\pi r^2$ each, and the side, unrolled, is a rectangle of dimensions $2\pi r$ by $h$. So
>
> $$
> A = 2\pi r^2 + 2\pi rh .
> $$
>
> The volume is $1$ L $= 1000$ cm³, so $\pi r^2 h = 1000$ and $h = 1000/(\pi r^2)$. Substituting,
>
> $$
> A(r) = 2\pi r^2 + 2\pi r \cdot \frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}, \qquad r > 0 .
> $$
>
> $r$ must be positive, and there is no upper limit on it.
>
> **Solve.**
>
> $$
> A'(r) = 4\pi r - \frac{2000}{r^2} = \frac{4(\pi r^3 - 500)}{r^2} ,
> $$
>
> so $A'(r) = 0$ when $\pi r^3 = 500$: the only critical number is $r = \sqrt[3]{500/\pi} \approx 5.42$. The domain $(0, \infty)$ has no endpoints, so the argument of [[§34 Optimization Problems#^ex-34-1|Example §34.1]] is not available. But $A'(r) < 0$ for $r < \sqrt[3]{500/\pi}$ and $A'(r) > 0$ for $r > \sqrt[3]{500/\pi}$: $A$ is decreasing for *all* $r$ to the left of the critical number and increasing for *all* $r$ to the right. By [[§34 Optimization Problems#^thm-34-1|Theorem §34.1]], $r = \sqrt[3]{500/\pi}$ gives the absolute minimum. (Alternatively: $A(r) \to \infty$ as $r \to 0^+$ and as $r \to \infty$, so there must be a minimum value, and it must occur at the critical number.)
>
> The corresponding height, using $\pi r^3 = 500$, is
>
> $$
> h = \frac{1000}{\pi r^2} = \frac{1000\,r}{\pi r^3} = \frac{1000\,r}{500} = 2r .
> $$
>
> So the radius should be $\sqrt[3]{500/\pi}$ cm and the height equal to twice the radius, that is, the diameter.
>
> **Alternative: implicit differentiation.** Keep both equations $A = 2\pi r^2 + 2\pi rh$ and $\pi r^2 h = 1000$, and differentiate both with respect to $r$, treating $A$ and $h$ as functions of $r$ ([[§21 Implicit Differentiation#^rem-21-1|Remark: Method — Implicit Differentiation]]):
>
> $$
> A' = 4\pi r + 2\pi r h' + 2\pi h, \qquad \pi r^2 h' + 2\pi r h = 0 .
> $$
>
> At the minimum $A' = 0$. Dividing the first equation by $2\pi$ and the second by $\pi r$ gives $2r + rh' + h = 0$ and $rh' + 2h = 0$; subtracting, $2r - h = 0$, so $h = 2r$.
>
> *Stewart: Example 4.7.2 and Notes 1–2*

^ex-34-2

> [!example] Example §34.3: The Closest Point on a Parabola
> Find the point on the parabola $y^2 = 2x$ that is closest to the point $(1, 4)$.
>
> The distance between $(1, 4)$ and a point $(x, y)$ is $d = \sqrt{(x - 1)^2 + (y - 4)^2}$. On the parabola $x = \frac12 y^2$, so
>
> $$
> d = \sqrt{\big(\tfrac12 y^2 - 1\big)^2 + (y - 4)^2} .
> $$
>
> (One could instead substitute $y = \sqrt{2x}$, but that misses the lower half of the parabola.) Since $\sqrt{\phantom{x}}$ is increasing, $d$ is smallest exactly where $d^2$ is smallest, and $d^2$ is easier to differentiate. So minimize
>
> $$
> f(y) = \big(\tfrac12 y^2 - 1\big)^2 + (y - 4)^2 ,
> $$
>
> where $y$ ranges over all real numbers. By the Chain Rule,
>
> $$
> f'(y) = 2\big(\tfrac12 y^2 - 1\big)\,y + 2(y - 4) = y^3 - 2y + 2y - 8 = y^3 - 8 .
> $$
>
> So $f'(y) = 0$ only at $y = 2$, with $f'(y) < 0$ for $y < 2$ and $f'(y) > 0$ for $y > 2$. By [[§34 Optimization Problems#^thm-34-1|Theorem §34.1]] the absolute minimum occurs at $y = 2$. (Geometrically it is clear that there is a closest point, though no farthest one.) The corresponding $x$ is $\frac12 y^2 = 2$. So the closest point is $(2, 2)$, at distance $d = \sqrt{f(2)} = \sqrt{1 + 4} = \sqrt5$.
>
> *Stewart: Example 4.7.3*

^ex-34-3

> [!example] Example §34.4: Row, Then Run
> A woman launches her boat from point $A$ on a bank of a straight river, $3$ km wide, and wants to reach point $B$, $8$ km downstream on the opposite bank, as quickly as possible. She can row her boat directly across the river to point $C$ and then run to $B$, or row directly to $B$, or row to some point $D$ between $C$ and $B$ and then run to $B$. She can row $6$ km/h and run $8$ km/h. Where should she land? (The speed of the water is negligible.)
>
> **Set up.** Let $x$ be the distance from $C$ to $D$. The running distance is $|DB| = 8 - x$, and by the Pythagorean Theorem the rowing distance is $|AD| = \sqrt{x^2 + 9}$. Since time $=$ distance$/$rate, the total time is
>
> $$
> T(x) = \frac{\sqrt{x^2 + 9}}{6} + \frac{8 - x}{8}, \qquad 0 \le x \le 8 .
> $$
>
> ($x = 0$ means rowing to $C$, and $x = 8$ rowing straight to $B$.)
>
> **Critical numbers.**
>
> $$
> T'(x) = \frac{x}{6\sqrt{x^2 + 9}} - \frac18 .
> $$
>
> Using $x \ge 0$,
>
> $$
> T'(x) = 0 \iff \frac{x}{6\sqrt{x^2 + 9}} = \frac18 \iff 4x = 3\sqrt{x^2 + 9} \iff 16x^2 = 9(x^2 + 9) \iff 7x^2 = 81 \iff x = \frac{9}{\sqrt7} .
> $$
>
> (Squaring is reversible here because both sides are $\ge 0$.)
>
> **Compare (Closed Interval Method).** With $x^2 + 9 = \frac{81}{7} + 9 = \frac{144}{7}$, so $\sqrt{x^2 + 9} = \frac{12}{\sqrt7}$,
>
> $$
> T(0) = \frac36 + 1 = 1.5, \qquad
> T\Big(\frac{9}{\sqrt7}\Big) = \frac{2}{\sqrt7} + 1 - \frac{9}{8\sqrt7} = 1 + \frac{7}{8\sqrt7} = 1 + \frac{\sqrt7}{8} \approx 1.33, \qquad
> T(8) = \frac{\sqrt{73}}{6} \approx 1.42 .
> $$
>
> The smallest is $T(9/\sqrt7)$, so the absolute minimum of $T$ occurs at $x = 9/\sqrt7$. She should land $9/\sqrt7$ km ($\approx 3.4$ km) downstream from her starting point.
>
> *Stewart: Example 4.7.4*

^ex-34-4

![[m233-31-1.svg]]
*[[§34 Optimization Problems#^ex-34-4|Example §34.4]]. Rowing from $A$ to a landing point $D$ at distance $x$ beyond $C$ takes $\sqrt{x^2 + 9}/6$ hours (red); running the remaining $8 - x$ km to $B$ takes $(8 - x)/8$ hours (green). The best landing point $x = 9/\sqrt7 \approx 3.4$ balances the two: there $\frac{x}{\sqrt{x^2 + 9}} = \frac68$, the ratio of the speeds.*

The choice of variable can make the calculus unnecessary. Stewart's Example 4.7.5 asks for the largest rectangle inscribed in a semicircle of radius $r$. With the corner $(x, y)$ on the circle, $A = 2x\sqrt{r^2 - x^2}$ on $[0, r]$, maximized at $x = r/\sqrt2$ with $A = r^2$. With the angle $\theta$ from the center to the corner, $A(\theta) = (2r\cos\theta)(r\sin\theta) = r^2\sin 2\theta$, whose maximum $r^2$ (at $\theta = \pi/4$) is evident.

## Applications to Business and Economics

> [!definition] Definition §34.1: Demand Function
> Let $C(x)$ be the **cost function**, the cost of producing $x$ units of a product; its derivative $C'(x)$ is the **marginal cost** ([[§23 Rates of Change in the Natural and Social Sciences#^def-23-10|Def. §23.10]]).
> - If $p(x)$ is the price per unit that the company can charge if it sells $x$ units, then $p$ is the **demand function** (or **price function**). One expects it to be decreasing.
>
> *Stewart: 4.7 (text)*

^def-34-1

> [!definition] Definition §34.2: Revenue Function
> - The **revenue function** is $R(x) = x\,p(x)$ (quantity $\times$ price), and its derivative $R'$ is the **marginal revenue function**.
>
> *Stewart: 4.7 (text)*

^def-34-2

> [!definition] Definition §34.3: Profit Function
> - The **profit function** is $P(x) = R(x) - C(x)$, and its derivative $P'$ is the **marginal profit function**.
>
> *Stewart: 4.7 (text)*

^def-34-3

> [!example] Example §34.5: Maximizing Revenue
> A store has been selling $200$ TV monitors a week at $\$350$ each. A market survey indicates that for each $\$10$ rebate offered to buyers, the number of monitors sold will increase by $20$ a week. Find the demand function and the revenue function. How large a rebate should the store offer to maximize revenue?
>
> **Demand function.** If $x$ monitors are sold per week, the increase in sales is $x - 200$. Each increase of $20$ units comes with a price decrease of $\$10$, so each additional unit sold lowers the price by $\frac{1}{20} \times 10$, and
>
> $$
> p(x) = 350 - \frac{10}{20}(x - 200) = 450 - \frac12 x .
> $$
>
> **Revenue function.**
>
> $$
> R(x) = x\,p(x) = 450x - \frac12 x^2 .
> $$
>
> **Maximize.** $R'(x) = 450 - x = 0$ when $x = 450$. Since $R' > 0$ for $x < 450$ and $R' < 0$ for $x > 450$, this gives the absolute maximum by [[§34 Optimization Problems#^thm-34-1|Theorem §34.1]] (or note that the graph of $R$ is a parabola opening downward). The corresponding price is $p(450) = 450 - 225 = 225$, so the rebate is $350 - 225 = 125$. To maximize revenue, the store should offer a rebate of $\$125$.
>
> *Stewart: Example 4.7.6*

^ex-34-5
