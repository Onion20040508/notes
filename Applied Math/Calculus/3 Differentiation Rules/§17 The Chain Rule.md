---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 17
stewart: "3.4"
aliases: ["Stewart 3.4"]
tags: [calculus]
---
← [[§16 Derivatives of Trigonometric Functions]] · ↑ [[· 3 Differentiation Rules]] · [[§18 Implicit Differentiation]] →

*Stewart, Section 3.4.*

The rules so far do not reach a function such as $F(x) = \sqrt{x^2 + 1}$. It is a composite $F = f \circ g$ of $f(u) = \sqrt{u}$ and $u = g(x) = x^2 + 1$ ([[§3 New Functions from Old Functions#^def-3-2|Definition §3.2]]), and both pieces can be differentiated. The Chain Rule says that the derivative of a composite is the product of the derivatives, each taken at the right point: $F'(x) = f'(g(x))\,g'(x)$. It is one of the most important differentiation rules. Combined with the earlier rules it differentiates every function built from the familiar ones, and it gives the derivative of $b^x$ for every base $b$.

## The Chain Rule

> [!remark] Remark: Why It Works
> Read derivatives as rates of change: $du/dx$ is the rate of change of $u$ with respect to $x$, $dy/du$ that of $y$ with respect to $u$, and $dy/dx$ that of $y$ with respect to $x$. If $u$ changes twice as fast as $x$, and $y$ changes three times as fast as $u$, then $y$ should change six times as fast as $x$. So we expect $dy/dx$ to be the product of $dy/du$ and $du/dx$.
>
> In terms of increments: let $\Delta u = g(x + \Delta x) - g(x)$ and $\Delta y = f(u + \Delta u) - f(u)$. It is tempting to write
>
> $$
> \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta u} \cdot \frac{\Delta u}{\Delta x} = \lim_{\Delta u \to 0} \frac{\Delta y}{\Delta u} \cdot \lim_{\Delta x \to 0} \frac{\Delta u}{\Delta x} = \frac{dy}{du}\,\frac{du}{dx} \qquad (3)
> $$
>
> (using $\Delta u \to 0$ as $\Delta x \to 0$, because $g$ is continuous). The only flaw is that $\Delta u$ may be $0$ even when $\Delta x \ne 0$, and then $\Delta y / \Delta u$ makes no sense. The proof below avoids ever dividing by $\Delta u$.

^rem-17-1

The proof rests on a reformulation of differentiability.

> [!theorem] Lemma §17.1: Differentiability in Increment Form
> Let $y = f(x)$ be differentiable at $a$, and for an increment $\Delta x$ let $\Delta y = f(a + \Delta x) - f(a)$. Then
>
> $$
> \Delta y = f'(a)\,\Delta x + \varepsilon\,\Delta x \qquad\text{where}\qquad \varepsilon \to 0 \text{ as } \Delta x \to 0, \qquad (6)
> $$
>
> and $\varepsilon$, as a function of $\Delta x$, is continuous at $\Delta x = 0$ with value $0$ there (Stewart: "$\varepsilon$ is a continuous function of $\Delta x$").
>
> *Stewart: 3.4, Equation 6*

^lem-17-1

> [!proof]+ Proof
> Define $\varepsilon$ as the difference between $\Delta y / \Delta x$ and $f'(a)$:
>
> $$
> \varepsilon = \frac{\Delta y}{\Delta x} - f'(a) \quad (\Delta x \ne 0), \qquad \varepsilon = 0 \quad (\Delta x = 0) .
> $$
>
> By the definition of the derivative,
>
> $$
> \lim_{\Delta x \to 0} \varepsilon = \lim_{\Delta x \to 0} \left( \frac{\Delta y}{\Delta x} - f'(a) \right) = f'(a) - f'(a) = 0 ,
> $$
>
> which equals the value of $\varepsilon$ at $\Delta x = 0$. So $\varepsilon$ is continuous at $\Delta x = 0$. For $\Delta x \ne 0$, multiplying the definition of $\varepsilon$ by $\Delta x$ gives $\Delta y = f'(a)\,\Delta x + \varepsilon\,\Delta x$. For $\Delta x = 0$ both sides are $0$.

^pf-17-1

*Uses:* [[§12 Derivatives and Rates of Change#^def-12-3|Def. §12.3]] (definition of $f'(a)$), [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]] (Limit Law 2)

> [!remark]- Connections
> - Equation 6 says that $f(a + \Delta x) \approx f(a) + f'(a)\,\Delta x$ with an error that is small *relative to* $\Delta x$: the linear approximation of [[§23 Linear Approximations and Differentials#^def-23-1|Definition §23.1]]. In several variables this becomes the definition of differentiability: [[§6 Differentiability#^def-6-1|452 Def. §6.1]].

> [!theorem] Theorem §17.2: The Chain Rule
> If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then the composite function $F = f \circ g$ defined by $F(x) = f(g(x))$ is differentiable at $x$, and $F'$ is given by the product
>
> $$
> F'(x) = f'(g(x)) \cdot g'(x) . \qquad (1)
> $$
>
> In Leibniz notation, if $y = f(u)$ and $u = g(x)$ are both differentiable functions, then
>
> $$
> \frac{dy}{dx} = \frac{dy}{du}\,\frac{du}{dx} . \qquad (2)
> $$
>
> *Stewart: 3.4, The Chain Rule (Formulas 1 and 2)*

^thm-17-2

> [!proof]+ Proof
> Let $u = g(x)$ be differentiable at $a$ and $y = f(u)$ differentiable at $b = g(a)$. Let $\Delta x$ be an increment in $x$, and $\Delta u$, $\Delta y$ the corresponding increments in $u$ and $y$:
>
> $$
> \Delta u = g(a + \Delta x) - g(a), \qquad \Delta y = f(b + \Delta u) - f(b) = f(g(a + \Delta x)) - f(g(a)) .
> $$
>
> By Lemma §17.1 applied to $g$ at $a$,
>
> $$
> \Delta u = g'(a)\,\Delta x + \varepsilon_1\,\Delta x = [g'(a) + \varepsilon_1]\,\Delta x , \qquad (7)
> $$
>
> where $\varepsilon_1 \to 0$ as $\Delta x \to 0$. By Lemma §17.1 applied to $f$ at $b$,
>
> $$
> \Delta y = f'(b)\,\Delta u + \varepsilon_2\,\Delta u = [f'(b) + \varepsilon_2]\,\Delta u , \qquad (8)
> $$
>
> where $\varepsilon_2$ is a function of $\Delta u$ that is continuous at $\Delta u = 0$ with value $0$ there. Equation 8 holds also when $\Delta u = 0$; this is why Lemma §17.1 sets $\varepsilon = 0$ at $0$. Substituting (7) into (8),
>
> $$
> \Delta y = [f'(b) + \varepsilon_2][g'(a) + \varepsilon_1]\,\Delta x, \qquad\text{so}\qquad \frac{\Delta y}{\Delta x} = [f'(b) + \varepsilon_2][g'(a) + \varepsilon_1] \quad (\Delta x \ne 0) .
> $$
>
> As $\Delta x \to 0$, Equation 7 shows $\Delta u \to 0$. Then $\varepsilon_2 \to 0$ as $\Delta x \to 0$: $\varepsilon_2$ is continuous at $0$ with value $0$, so the limit of the composite is $0$ by [[§10 Continuity#^thm-10-7|Theorem §10.7]]. (Stewart says only "$\varepsilon_2 \to 0$ as $\Delta u \to 0$"; the continuity is what makes the step valid even when $\Delta u = 0$ for some $\Delta x \ne 0$.) Taking the limit,
>
> $$
> \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} [f'(b) + \varepsilon_2][g'(a) + \varepsilon_1] = f'(b)\,g'(a) = f'(g(a))\,g'(a) .
> $$

^pf-17-2

*Uses:* [[§17 The Chain Rule#^lem-17-1|§17.1]], [[§10 Continuity#^thm-10-7|§10.7]], [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]] (Limit Laws 1 and 4)

> [!remark]- Connections
> - Rigorous treatment: [[§28 Basic Properties of the Derivative#^thm-28-3|451 Thm. §28.3]]. Its first proof is the tempting argument (3) and fails for the same reason; its second proof replaces $\Delta y / \Delta u$ by a function that is continuous at $f(a)$ (in 451 the inner function is $f$, so this is the point $b = g(a)$ here), which is $f'(b) + \varepsilon_2$ in the proof of Theorem §17.2.
> - Several variables: [[§6 Differentiability#^thm-6-9|452 Thm. §6.9]], and in Calculus [[§94 The Chain Rule#^thm-94-3|Theorem §94.3]] (Stewart 14.5).
> - Complex-variables version: [[§20 Rules for Differentiation#^thm-20-4|342 Thm. §20.4]] (the same formula for complex derivatives).

> [!remark] Remark: Reading the Leibniz Form
> Formula 2 is easy to remember: think of $dy/du$ and $du/dx$ as quotients and "cancel" $du$. But $du$ has not been defined, and $du/dx$ is not an actual quotient. Also, $dy/dx$ and $dy/du$ are different derivatives of the same quantity $y$: in $dy/dx$, $y$ is a function of $x$ ($y = \sqrt{x^2 + 1}$ in Example §17.1); in $dy/du$, $y$ is a function of $u$ ($y = \sqrt{u}$). So
>
> $$
> \frac{dy}{dx} = F'(x) = \frac{x}{\sqrt{x^2 + 1}} \qquad\text{whereas}\qquad \frac{dy}{du} = f'(u) = \frac{1}{2\sqrt{u}} .
> $$

^rem-17-2

> [!remark] Remark: Method — Applying the Chain Rule
> 1. **Find the layers.** Write the function as $f(g(x))$: the *outer* function $f$ is the last operation applied, the *inner* function $g$ is what it is applied to. (In $\sin(x^2)$ the outer function is sine; in $\sin^2 x = (\sin x)^2$ it is squaring.)
> 2. **Work from the outside in.** Differentiate the outer function, evaluate it *at the inner function* (leave the inside unchanged), then multiply by the derivative of the inner function:
>
> $$
> \frac{d}{dx}\,\underbrace{f}_{\text{outer}}\big(\underbrace{g(x)}_{\text{inner}}\big) = \underbrace{f'}_{\text{derivative of outer}}\big(\underbrace{g(x)}_{\text{at inner}}\big) \cdot \underbrace{g'(x)}_{\text{derivative of inner}} .
> $$
>
> 3. **Longer chains.** If the inner function is itself a composite, repeat. For $y = f(u)$, $u = g(x)$, $x = h(t)$, applying the Chain Rule twice gives
>
> $$
> \frac{dy}{dt} = \frac{dy}{dx}\,\frac{dx}{dt} = \frac{dy}{du}\,\frac{du}{dx}\,\frac{dx}{dt} .
> $$
>
> This "chain" of links gives the rule its name.
> 4. **Combine with the other rules.** A product or quotient of composites needs the Product or Quotient Rule first ([[§15 The Product and Quotient Rules#^thm-15-1|Theorems §15.1]] and [[§15 The Product and Quotient Rules#^thm-15-2|§15.2]]), then the Chain Rule on each factor.
> 5. **Simplify** by factoring out common powers.

^rem-17-3

> [!example] Example §17.1: Two Ways to Write the Chain Rule
> Find $F'(x)$ if $F(x) = \sqrt{x^2 + 1}$.
>
> **Solution 1 (Formula 1).** $F(x) = f(g(x))$ with $f(u) = \sqrt{u}$ and $g(x) = x^2 + 1$. Since
>
> $$
> f'(u) = \tfrac12 u^{-1/2} = \frac{1}{2\sqrt{u}} \qquad\text{and}\qquad g'(x) = 2x ,
> $$
>
> $$
> F'(x) = f'(g(x)) \cdot g'(x) = \frac{1}{2\sqrt{x^2 + 1}} \cdot 2x = \frac{x}{\sqrt{x^2 + 1}} .
> $$
>
> **Solution 2 (Formula 2).** With $u = x^2 + 1$ and $y = \sqrt{u}$,
>
> $$
> F'(x) = \frac{dy}{du}\,\frac{du}{dx} = \frac{1}{2\sqrt{u}}\,(2x) = \frac{1}{2\sqrt{x^2 + 1}}\,(2x) = \frac{x}{\sqrt{x^2 + 1}} .
> $$
>
> *Stewart: Example 3.4.1*

^ex-17-1

> [!example] Example §17.2: Which Function Is Outside?
> Differentiate (a) $y = \sin(x^2)$ and (b) $y = \sin^2 x$.
>
> **(a)** The outer function is sine and the inner function is squaring:
>
> $$
> \frac{dy}{dx} = \frac{d}{dx} \sin(x^2) = \cos(x^2) \cdot 2x = 2x\cos(x^2) .
> $$
>
> **(b)** $\sin^2 x = (\sin x)^2$: now the outer function is squaring and the inner function is sine:
>
> $$
> \frac{dy}{dx} = \frac{d}{dx} (\sin x)^2 = 2 (\sin x) \cdot \cos x = 2\sin x\cos x .
> $$
>
> The answer can also be written $\sin 2x$, by the double-angle formula.
>
> *Stewart: Example 3.4.2*

^ex-17-2

## Special Cases

In Example §17.2(a) the Chain Rule was combined with the rule for sine. The same combination works for every differentiation formula.

> [!theorem] Corollary §17.3: The Power Rule Combined with the Chain Rule
> If $n$ is any real number and $u = g(x)$ is differentiable, then
>
> $$
> \frac{d}{dx}(u^n) = n u^{n-1} \frac{du}{dx} .
> $$
>
> Alternatively, $\dfrac{d}{dx}[g(x)]^n = n[g(x)]^{n-1} \cdot g'(x)$.
>
> *Stewart: 3.4, Rule 4*

^cor-17-3

> [!proof]+ Proof
> Write $y = [g(x)]^n$ as $y = f(u) = u^n$ with $u = g(x)$. By the Chain Rule and the Power Rule (for real $n$, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-6|Theorem §19.6]]),
>
> $$
> \frac{dy}{dx} = \frac{dy}{du}\,\frac{du}{dx} = n u^{n-1} \frac{du}{dx} = n[g(x)]^{n-1} g'(x) .
> $$
>
> (For non-integer $n$ this holds at the $x$ where $u^{n-1}$ is defined.)

^pf-17-3

*Uses:* [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|§14.2]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-6|§19.6]] (Power Rule, general version)

Example §17.1 is the case $n = \frac12$. For instance, $\frac{d}{dx}(x^3 - 1)^{100} = 100(x^3 - 1)^{99} \cdot 3x^2 = 300x^2(x^3 - 1)^{99}$.

> [!theorem] Corollary §17.4: Sine and the Exponential of a Function
> If $u$ is a differentiable function of $x$, then
>
> $$
> \frac{d}{dx}(\sin u) = \cos u\,\frac{du}{dx}, \qquad \frac{d}{dx}(e^u) = e^u \frac{du}{dx} .
> $$
>
> Likewise every trigonometric formula of [[§16 Derivatives of Trigonometric Functions#^thm-16-4|Theorem §16.4]] combines with the Chain Rule, e.g. $\frac{d}{dx}(\sec u) = \sec u \tan u\,\frac{du}{dx}$.
>
> *Stewart: 3.4 (text and margin)*

^cor-17-4

> [!proof]+ Proof
> With $y = \sin u$, the Chain Rule gives $\dfrac{dy}{dx} = \dfrac{dy}{du}\,\dfrac{du}{dx} = \cos u\,\dfrac{du}{dx}$ by [[§16 Derivatives of Trigonometric Functions#^thm-16-1|Theorem §16.1]]. With $y = e^u$, $\dfrac{dy}{du} = e^u$ by [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|Theorem §14.6]]. The other formulas are the same.

^pf-17-4

*Uses:* [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§16 Derivatives of Trigonometric Functions#^thm-16-1|§16.1]], [[§16 Derivatives of Trigonometric Functions#^thm-16-4|§16.4]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|§14.6]]

For instance, $\frac{d}{dx}(e^{\sin x}) = e^{\sin x} \cos x$.

> [!example] Example §17.3: Combining with the Product and Quotient Rules
> **(a)** Find the derivative of $g(t) = \left( \dfrac{t - 2}{2t + 1} \right)^9$.
>
> By Corollary §17.3 and then the Quotient Rule,
>
> $$
> g'(t) = 9 \left( \frac{t - 2}{2t + 1} \right)^8 \frac{d}{dt} \left( \frac{t - 2}{2t + 1} \right)
> = 9 \left( \frac{t - 2}{2t + 1} \right)^8 \frac{(2t + 1) \cdot 1 - 2(t - 2)}{(2t + 1)^2}
> = 9 \cdot \frac{(t - 2)^8}{(2t + 1)^8} \cdot \frac{5}{(2t + 1)^2} = \frac{45(t - 2)^8}{(2t + 1)^{10}} .
> $$
>
> **(b)** Differentiate $y = (2x + 1)^5 (x^3 - x + 1)^4$.
>
> Here the Product Rule comes first, then the Chain Rule on each factor:
>
> $$
> \begin{aligned}
> \frac{dy}{dx} &= (2x + 1)^5 \frac{d}{dx}(x^3 - x + 1)^4 + (x^3 - x + 1)^4 \frac{d}{dx}(2x + 1)^5 \\
> &= (2x + 1)^5 \cdot 4(x^3 - x + 1)^3 (3x^2 - 1) + (x^3 - x + 1)^4 \cdot 5(2x + 1)^4 \cdot 2 .
> \end{aligned}
> $$
>
> Each term has the factor $2(2x + 1)^4 (x^3 - x + 1)^3$. What remains is $2(2x + 1)(3x^2 - 1) + 5(x^3 - x + 1) = (12x^3 + 6x^2 - 4x - 2) + (5x^3 - 5x + 5)$, so
>
> $$
> \frac{dy}{dx} = 2(2x + 1)^4 (x^3 - x + 1)^3 (17x^3 + 6x^2 - 9x + 3) .
> $$
>
> *Stewart: Examples 3.4.5 and 3.4.6*

^ex-17-3

> [!example] Example §17.4: Chains of Three Links
> **(a)** If $f(x) = \sin(\cos(\tan x))$, the Chain Rule is used twice:
>
> $$
> f'(x) = \cos(\cos(\tan x)) \frac{d}{dx} \cos(\tan x) = \cos(\cos(\tan x)) [-\sin(\tan x)] \frac{d}{dx}(\tan x) = -\cos(\cos(\tan x)) \sin(\tan x) \sec^2 x .
> $$
>
> **(b)** Differentiate $y = e^{\sec 3\theta}$. The outer function is the exponential, the middle one is secant, and the inner one is tripling:
>
> $$
> \frac{dy}{d\theta} = e^{\sec 3\theta} \frac{d}{d\theta}(\sec 3\theta) = e^{\sec 3\theta} \sec 3\theta \tan 3\theta \frac{d}{d\theta}(3\theta) = 3e^{\sec 3\theta} \sec 3\theta \tan 3\theta .
> $$
>
> *Stewart: Examples 3.4.8 and 3.4.9*

^ex-17-4

## Derivatives of General Exponential Functions

> [!theorem] Theorem §17.5: Derivative of an Exponential Function with Base b
> For every base $b > 0$,
>
> $$
> \frac{d}{dx}(b^x) = b^x \ln b . \qquad (5)
> $$
>
> Do not confuse this (where $x$ is the *exponent*) with the Power Rule $\frac{d}{dx}(x^n) = nx^{n-1}$ (where $x$ is the *base*).
>
> *Stewart: 3.4, Formula 5*

^thm-17-5

> [!proof]+ Proof
> Since $e^{\ln b} = b$, we can write $b^x = (e^{\ln b})^x = e^{(\ln b)x}$ ([[§5 Inverse Functions and Logarithms#^prop-5-7|Proposition §5.7]], Equation 1.5.10). By Corollary §17.4 with $u = (\ln b)x$, and because $\ln b$ is a constant,
>
> $$
> \frac{d}{dx}(b^x) = \frac{d}{dx}\big(e^{(\ln b)x}\big) = e^{(\ln b)x} \frac{d}{dx}\big[(\ln b)x\big] = e^{(\ln b)x} (\ln b) = b^x \ln b .
> $$

^pf-17-5

*Uses:* [[§5 Inverse Functions and Logarithms#^prop-5-7|§5.7]] (Equation 1.5.10), [[§17 The Chain Rule#^cor-17-4|§17.4]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-3|§14.3]]

*From the integral definition of $\ln$ in Appendix G: [[§121 The Logarithm Defined as an Integral#^thm-121-10|Theorem §121.10]].*

Comparing with [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-5|Theorem §14.5]]: the constant $f'(0) = \lim_{h \to 0} (b^h - 1)/h$ is $\ln b$.

> [!example] Example §17.5: Exponentials with Other Bases
> Find the derivative of (a) $g(x) = 2^x$ and (b) $h(x) = 5^{x^2}$.
>
> **(a)** By Formula 5 with $b = 2$, $g'(x) = 2^x \ln 2$. This agrees with the estimate $\frac{d}{dx}(2^x) \approx (0.693)2^x$ of [[§14 Derivatives of Polynomials and Exponential Functions#^rem-14-2|Remark: The Constants for Base 2 and Base 3]], because $\ln 2 \approx 0.693147$.
>
> **(b)** The outer function is the exponential with base $5$ and the inner function is squaring, so by Formula 5 and the Chain Rule
>
> $$
> h'(x) = 5^{x^2} \ln 5 \cdot \frac{d}{dx}(x^2) = 2x \cdot 5^{x^2} \ln 5 .
> $$
>
> *Stewart: Example 3.4.10*

^ex-17-5
