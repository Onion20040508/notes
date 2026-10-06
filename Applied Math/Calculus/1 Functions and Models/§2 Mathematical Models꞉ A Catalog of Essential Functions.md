---
type: section
subject: "[[Calculus]]"
chapter: 1
section: 2
stewart: "1.2"
aliases: ["Stewart 1.2"]
tags: [calculus]
---
← [[§1 Four Ways to Represent a Function]] · ↑ [[· 1 Functions and Models]] · [[§3 New Functions from Old Functions]] →

*Stewart, Section 1.2.*

A mathematical model describes a real-world phenomenon by a function. This section explains how such models are built and tested, and then catalogs the functions used most often, which recur throughout the course: linear functions, polynomials, power functions (roots and reciprocals included), rational and algebraic functions, and the transcendental functions (trigonometric, exponential and logarithmic). For each family, know the formula, the domain and the shape of the graph.

## Mathematical Models

> [!definition] Definition §2.1: Mathematical Model
> A **mathematical model** is a mathematical description, often by means of a function or an equation, of a real-world phenomenon: the size of a population, the demand for a product, the speed of a falling object, the concentration of a product in a chemical reaction, the life expectancy of a person at birth, the cost of emissions reductions. Its purpose is to understand the phenomenon and perhaps to predict its future behavior.
>
> A model is never a completely accurate representation of a physical situation: it is an *idealization*. A good model simplifies reality enough to permit calculation, yet is accurate enough to give valuable conclusions.
>
> *Stewart: 1.2 (text)*

^def-2-1

> [!remark] Remark: Method — The Modeling Process
> 1. **Formulate.** Identify and name the independent and dependent variables, and make assumptions that simplify the phenomenon enough to be mathematically tractable. Use a physical law if there is one. If not, collect data, tabulate it, plot it, and look for a pattern that suggests a formula.
> 2. **Solve.** Apply mathematics (such as calculus) to the model to derive mathematical conclusions.
> 3. **Interpret.** Translate the conclusions back into statements about the real phenomenon: explanations or predictions.
> 4. **Test.** Check the predictions against new real data. If they do not compare well, refine the model or formulate a new one, and start the cycle again.

^rem-2-1

## Linear Models

> [!definition] Definition §2.2: Linear Function
> $y$ is a **linear function** of $x$ if the graph of the function is a line. Then, by the slope-intercept form of the equation of a line,
>
> $$
> y = f(x) = mx + b ,
> $$
>
> where $m$ is the slope of the line and $b$ is its $y$-intercept.
>
> *Stewart: 1.2 (text)*

^def-2-2

> [!theorem] Proposition §2.1: Linear Functions Change at a Constant Rate
> If $f(x) = mx + b$, then for all $x_1 \ne x_2$
>
> $$
> \frac{f(x_2) - f(x_1)}{x_2 - x_1} = m .
> $$
>
> So the change in $f(x)$ is always $m$ times the change in $x$: the slope $m$ is the rate of change of $y$ with respect to $x$. For example, for $f(x) = 3x - 2$, whenever $x$ increases by $0.1$, $f(x)$ increases by $0.3$.
>
> *Stewart: 1.2 (text)*

^prop-2-1

> [!proof]+ Proof
> $f(x_2) - f(x_1) = (mx_2 + b) - (mx_1 + b) = m(x_2 - x_1)$. Divide by $x_2 - x_1 \ne 0$.

^pf-2-1

*Uses:* [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-2|Def. §2.2]]

> [!example] Example §2.1: A Linear Model from a Physical Assumption
> As dry air moves upward, it expands and cools. The ground temperature is $20^\circ$C, and the temperature at a height of $1$ km is $10^\circ$C. (a) Express the temperature $T$ (in $^\circ$C) as a function of the height $h$ (in km), assuming that a linear model is appropriate. (b) What does the slope represent? (c) What is the temperature at a height of $2.5$ km?
>
> **(a)** Since $T$ is assumed linear in $h$, $T = mh + b$. $T = 20$ when $h = 0$ gives $20 = m \cdot 0 + b = b$. $T = 10$ when $h = 1$ gives $10 = m \cdot 1 + 20$, so $m = 10 - 20 = -10$. Hence
>
> $$
> T = -10h + 20 .
> $$
>
> **(b)** The slope $m = -10\ ^\circ\text{C/km}$ is the rate of change of temperature with respect to height ([[§2 Mathematical Models꞉ A Catalog of Essential Functions#^prop-2-1|Proposition §2.1]]): the air cools by $10^\circ$C for each kilometer of height. The graph is a line falling from $(0, 20)$, crossing the $h$-axis at $h = 2$.
>
> **(c)** $T = -10(2.5) + 20 = -5^\circ$C.
>
> *Stewart: Example 1.2.1*

^ex-2-1

> [!definition] Definition §2.3: Empirical Model
> An **empirical model** is a model based entirely on collected data, used when no physical law or principle is available. One seeks a curve that "fits" the data, in the sense that it captures their basic trend.
>
> For data that lie close to a line, the standard choice is the **regression line**, found by the *method of least squares*: it minimizes the sum of the squares of the vertical distances between the data points and the line (Exercise 14.7.61, [[§96 Maximum and Minimum Values|§96]]). Calculators and software compute it (*linear regression*).
>
> *Stewart: 1.2 (text and margin note)*

^def-2-3

> [!remark]- Connections
> - Matrix version: [[§45 Applications to Linear Models#^def-45-new1|235 Def. §45.2]] and [[§45 Applications to Linear Models#^prop-45-1|235 Prop. §45.1]] (the regression line is the least-squares solution of $X\boldsymbol\beta = \mathbf{y}$, found from the normal equations [[§44 Least-Squares Problems#^thm-44-1|235 Thm. §44.1]]), worked in [[§45 Applications to Linear Models#^ex-45-1|235 Ex. §45.1]]; the quadratic fit of [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^ex-2-3|Example §2.3]] is the design matrix of [[§45 Applications to Linear Models#^ex-45-2|235 Ex. §45.2]](a).

> [!example] Example §2.2: An Empirical Linear Model for CO₂
> The average carbon dioxide level in the atmosphere, measured at Mauna Loa Observatory (in parts per million), was:
>
> | year | 1980 | 1984 | 1988 | 1992 | 1996 | 2000 | 2004 | 2008 | 2012 | 2016 |
> |---|---|---|---|---|---|---|---|---|---|---|
> | CO₂ (ppm) | 338.7 | 344.4 | 351.5 | 356.3 | 362.4 | 369.4 | 377.5 | 385.6 | 393.8 | 404.2 |
>
> Find a model for the CO₂ level $C$ as a function of the year $t$, and use it to estimate the level in 1987, to predict it for 2025, and to predict when it will exceed $440$ ppm.
>
> **Choosing a model.** A scatter plot of the data shows points close to a straight line, so a linear model is natural. One candidate is the line through the first and last data points. Its slope is
>
> $$
> \frac{404.2 - 338.7}{2016 - 1980} = \frac{65.5}{36} \approx 1.819 ,
> $$
>
> so its equation is $C - 338.7 = 1.819(t - 1980)$, or
>
> $$
> C = 1.819t - 3262.92 . \qquad (1)
> $$
>
> This line lies above most of the actual data points. The regression line fits better; a calculator gives slope $m = 1.78242$ and intercept $b = -3192.90$, so the least squares model is
>
> $$
> C = 1.78242t - 3192.90 . \qquad (2)
> $$
>
> **Interpolation** (estimating a value *between* observations): by (2),
>
> $$
> C(1987) = 1.78242(1987) - 3192.90 \approx 348.77 .
> $$
>
> (The observatory reported $348.93$ ppm for 1987, so the estimate is quite accurate.)
>
> **Extrapolation** (predicting *outside* the observed time frame, so far less certain):
>
> $$
> C(2025) = 1.78242(2025) - 3192.90 \approx 416.50 .
> $$
>
> **Exceeding 440 ppm.** $1.78242t - 3192.90 > 440$ means $1.78242t > 3632.9$, that is,
>
> $$
> t > \frac{3632.9}{1.78242} \approx 2038.18 .
> $$
>
> So the model predicts that the level will exceed $440$ ppm by 2038. This prediction is risky: it lies far from the observations, and the data show the level rising faster in recent years than the line does, so the actual crossing may come well before 2038.
>
> *Stewart: Examples 1.2.2 and 1.2.3*

^ex-2-2

## Polynomials

> [!definition] Definition §2.4: Polynomial
> A function $P$ is a **polynomial** if
>
> $$
> P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_2 x^2 + a_1 x + a_0 ,
> $$
>
> where $n$ is a nonnegative integer and the numbers $a_0, a_1, \ldots, a_n$ are constants, the **coefficients** of the polynomial. The domain of every polynomial is $\mathbb{R} = (-\infty, \infty)$. If the **leading coefficient** $a_n$ is not $0$, the **degree** of the polynomial is $n$. For example, $P(x) = 2x^6 - x^4 + \frac25 x^3 + \sqrt2$ has degree $6$.
> - Degree $1$: $P(x) = mx + b$, a linear function ([[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-2|Definition §2.2]]).
> - Degree $2$: $P(x) = ax^2 + bx + c$, a **quadratic function**. Its graph is a parabola, obtained by shifting the parabola $y = ax^2$ ([[§3 New Functions from Old Functions#^ex-3-2|Ex. §3.2]]); it opens upward if $a > 0$ and downward if $a < 0$.
> - Degree $3$: $P(x) = ax^3 + bx^2 + cx + d$ with $a \ne 0$, a **cubic function**.
>
> *Stewart: 1.2 (text)*

^def-2-4

> [!remark]- Connections
> - Developed further in: [[§4 Span and Linear Independence#^ladr-2-10|LADR 2.10]] and [[§4 Span and Linear Independence#^ladr-2-11|LADR 2.11]] (polynomials over $\mathbb{R}$ or $\mathbb{C}$ and their degree). That the coefficients, hence the degree, are determined by the function is [[§13 Polynomials#^ladr-4-8|LADR 4.8]]: a nonzero polynomial of degree $m$ has at most $m$ zeros.

Polynomials model many quantities in the natural and social sciences; for instance, economists often take a polynomial $P(x)$ for the cost of producing $x$ units of a commodity ([[§20 Rates of Change in the Natural and Social Sciences#^def-20-7|Definition §20.7]]).

> [!example] Example §2.3: A Quadratic Model for a Falling Ball
> A ball is dropped from the upper observation deck of the CN Tower, $450$ m above the ground, and its height $h$ above the ground is recorded at 1-second intervals:
>
> | $t$ (s) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
> |---|---|---|---|---|---|---|---|---|---|---|
> | $h$ (m) | 450 | 445 | 431 | 408 | 375 | 332 | 279 | 216 | 143 | 61 |
>
> Find a model that fits the data, and use it to predict when the ball hits the ground.
>
> **The model.** The scatter plot is clearly not a line: the drops per second grow ($5, 14, 23, 33, \ldots$). The points do look like part of a parabola, so try a quadratic model. Least squares (by calculator or computer algebra system) gives
>
> $$
> h = 449.36 + 0.96t - 4.90t^2 . \qquad (3)
> $$
>
> It fits very well; for instance at $t = 9$ it gives $449.36 + 8.64 - 396.90 = 61.10$, against the measured $61$.
>
> **Hitting the ground.** Solve $h = 0$, that is, $-4.90t^2 + 0.96t + 449.36 = 0$. By the quadratic formula,
>
> $$
> t = \frac{-0.96 \pm \sqrt{(0.96)^2 - 4(-4.90)(449.36)}}{2(-4.90)} = \frac{-0.96 \pm \sqrt{8808.3776}}{-9.80} \approx \frac{-0.96 \pm 93.853}{-9.80} .
> $$
>
> The roots are $t \approx 9.67$ and $t \approx -9.48$. Only the positive one is meaningful, so the model predicts that the ball hits the ground after about $9.7$ seconds.
>
> *Stewart: Example 1.2.4*

^ex-2-3

*Chain:* [[§13a The Parabola y = x², the CN Tower Ball, (√(t² + 9) − 3)∕t² and x³ − x#The Ball Dropped from the CN Tower|Chapter 2]] →

## Power Functions

> [!definition] Definition §2.5: Power Function
> A function of the form $f(x) = x^a$, where $a$ is a constant, is a **power function**. The important cases are
> 1. $a = n$, a positive integer: $x, x^2, x^3, \ldots$ (polynomials with one term);
> 2. $a = 1/n$, $n$ a positive integer: the root functions ([[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-6|Definition §2.6]]);
> 3. $a = -1$: the reciprocal function, and $a = -2$: inverse square laws ([[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-7|Definition §2.7]] and [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-new1|Definition §2.7]]).
>
> *Stewart: 1.2 (text)*

^def-2-5

> [!theorem] Proposition §2.2: Shape of the Graph of xⁿ
> Let $n$ be a positive integer and $f(x) = x^n$.
> 1. If $n$ is even, $f$ is an even function and its graph is similar to the parabola $y = x^2$. If $n$ is odd, $f$ is an odd function and its graph is similar to that of $y = x^3$.
> 2. All these graphs pass through $(0, 0)$ and $(1, 1)$. As $n$ increases, the graph of $y = x^n$ becomes flatter near $0$ and steeper when $|x| \ge 1$: for $0 < |x| < 1$, $|x|^{n+1} < |x|^n$, and for $|x| > 1$, $|x|^{n+1} > |x|^n$.
>
> *Stewart: 1.2 (text)*

^prop-2-2

> [!proof]+ Proof
> **1.** $f(-x) = (-x)^n = (-1)^n x^n$, and $(-1)^n = 1$ for even $n$, $-1$ for odd $n$. So $f(-x) = f(x)$ for even $n$ and $f(-x) = -f(x)$ for odd $n$ ([[§1 Four Ways to Represent a Function#^def-1-7|Def. §1.7]]). By [[§1 Four Ways to Represent a Function#^prop-1-2|Proposition §1.2]], the graph is symmetric about the $y$-axis (like $x^2$) or about the origin (like $x^3$). For $x \ge 0$ both kinds of graph rise from $0$, since $x^n$ is increasing on $[0, \infty)$ ([[§1 Four Ways to Represent a Function#^def-1-8|Def. §1.8]]): if $0 \le x_1 < x_2$ and $x_1^k < x_2^k$, then $x_1^{k+1} = x_1 x_1^k \le x_1 x_2^k < x_2 x_2^k = x_2^{k+1}$ (using $x_1 \ge 0$ and $x_2^k > 0$), so $x_1^n < x_2^n$ by induction on $k$.
>
> **2.** $0^n = 0$ and $1^n = 1$. Since $|x^n| = |x|^n$ and $|x|^{n+1} = |x| \cdot |x|^n$ with $|x|^n > 0$ for $x \ne 0$: if $|x| < 1$ the factor $|x|$ makes the product smaller, and if $|x| > 1$ it makes it larger. (If $x$ is small, $x^2$ is smaller, $x^3$ smaller still, and so on.)

^pf-2-2

*Uses:* [[§1 Four Ways to Represent a Function#^def-1-7|Def. §1.7]], [[§1 Four Ways to Represent a Function#^prop-1-2|§1.2]], [[§1 Four Ways to Represent a Function#^def-1-8|Def. §1.8]]

![[m233-2-1.svg]]
*Two families of power functions. (a) Even powers: $x^2$, $x^4$, $x^6$ all pass through $(-1, 1)$, $(0, 0)$ and $(1, 1)$, are symmetric about the $y$-axis, and the higher the power the flatter the graph between $-1$ and $1$ and the steeper outside. (b) Odd powers $x^3$, $x^5$: the same, with symmetry about the origin and $(-1, -1)$ in place of $(-1, 1)$.*

> [!definition] Definition §2.6: Root Function
> For a positive integer $n$, the function $f(x) = x^{1/n} = \sqrt[n]{x}$ is a **root function**.
> - $n$ even: the domain is $[0, \infty)$. For $n = 2$ this is the square root function $\sqrt{x}$, whose graph is the upper half of the parabola $x = y^2$; the graph of $\sqrt[n]{x}$ for other even $n$ looks similar.
> - $n$ odd: the domain is $\mathbb{R}$, since every real number has an $n$th root. For $n = 3$ this is the cube root function $\sqrt[3]{x}$; the graph of $\sqrt[n]{x}$ for odd $n > 3$ looks similar.
>
> *Stewart: 1.2 (text)*

^def-2-6

> [!definition] Definition §2.7: Reciprocal Function
> - The **reciprocal function** is $f(x) = x^{-1} = 1/x$. Its graph, $y = 1/x$ or $xy = 1$, is a hyperbola with the coordinate axes as asymptotes. It models quantities that are inversely proportional, such as **Boyle's Law**: at constant temperature, the volume $V$ of a gas is inversely proportional to the pressure $P$, $V = C/P$ with $C$ a constant.
>
> *Stewart: 1.2 (text)*

^def-2-7

> [!definition] Definition §2.7: Inverse Square Law
> - A model of the form $f(x) = C/x^2$ ($a = -2$) is an **inverse square law**: the first quantity is inversely proportional to the square of the second. For instance, the illumination $I$ of an object by a light source is $I = C/x^2$, where $x$ is the distance from the source. Gravitational force, loudness of sound and the electrostatic force between two charged particles obey inverse square laws.
>
> *Stewart: 1.2 (text)*

^def-2-new1

## Rational Functions

> [!definition] Definition §2.8: Rational Function
> A **rational function** is a ratio of two polynomials,
>
> $$
> f(x) = \frac{P(x)}{Q(x)} ,
> $$
>
> with $P$ and $Q$ polynomials. Its domain consists of all $x$ with $Q(x) \ne 0$. For example, $1/x$ has domain $\{x \mid x \ne 0\}$, and
>
> $$
> f(x) = \frac{2x^4 - x^2 + 1}{x^2 - 4}
> $$
>
> has domain $\{x \mid x \ne \pm 2\}$.
>
> *Stewart: 1.2 (text)*

^def-2-8

## Algebraic Functions

> [!definition] Definition §2.9: Algebraic and Transcendental Functions
> A function is **algebraic** if it can be constructed from polynomials using algebraic operations: addition, subtraction, multiplication, division and taking roots. Every rational function is algebraic. Further examples:
>
> $$
> f(x) = \sqrt{x^2 + 1}, \qquad g(x) = \frac{x^4 - 16x^2}{x + \sqrt{x}} + (x - 2)\sqrt[3]{x + 1} ,
> $$
>
> and, from relativity, the mass of a particle with velocity $v$, $m = f(v) = \dfrac{m_0}{\sqrt{1 - v^2/c^2}}$, where $m_0$ is the rest mass and $c = 3.0 \times 10^5$ km/s is the speed of light in a vacuum.
>
> Functions that are not algebraic are **transcendental**. These include the trigonometric, exponential and logarithmic functions.
>
> *Stewart: 1.2 (text)*

^def-2-9

> [!remark]- Connections
> - The same distinction for numbers: [[§2 The Set ℚ of Rational Numbers#^def-2-5|451 Def. §2.5]] (algebraic number) and [[§2 The Set ℚ of Rational Numbers#^def-2-10|451 Def. §2.10]] (transcendental number).

## Trigonometric Functions

Trigonometry is reviewed on Stewart's Reference Page 2 and in Appendix D. In calculus **radian measure** is always used unless otherwise indicated: $\sin x$ means the sine of the angle whose radian measure is $x$. By Appendix D, if the angle $x$ is placed in standard position and $(a, b)$ is a point other than the origin on its terminal side, at distance $r = \sqrt{a^2 + b^2}$ from the origin, then $\sin x = b/r$, $\cos x = a/r$ and $\tan x = b/a$. Sine and cosine have domain $(-\infty, \infty)$.

> [!theorem] Theorem §2.3: Bounds for Sine and Cosine
> For all values of $x$,
>
> $$
> -1 \le \sin x \le 1, \qquad -1 \le \cos x \le 1 ,
> $$
>
> or, in terms of absolute values, $|\sin x| \le 1$ and $|\cos x| \le 1$. The range of both sine and cosine is the closed interval $[-1, 1]$.
>
> *Stewart: 1.2 (boxed)*

^thm-2-3

> [!proof]+ Proof
> Stewart reads this off the graphs; it follows at once from the definitions recalled above. With $(a, b)$ on the terminal side at distance $r = \sqrt{a^2 + b^2} > 0$, we have $|b| = \sqrt{b^2} \le \sqrt{a^2 + b^2} = r$, so $|\sin x| = |b|/r \le 1$; likewise $|a| \le r$ gives $|\cos x| \le 1$.
>
> For the range, take $r = 1$: then $(\cos x, \sin x)$ is the point of the unit circle at angle $x$. As $x$ runs over $[0, 2\pi]$, this point runs once around the circle, and its coordinates take every value in $[-1, 1]$.

^pf-2-3

*Uses:* [[§119 Trigonometry#^def-119-4|Def. §119.4]] (trigonometric functions of a general angle)

> [!theorem] Theorem §2.4: Periodicity
> Sine and cosine are **periodic** with period $2\pi$: for all values of $x$,
>
> $$
> \sin(x + 2\pi) = \sin x, \qquad \cos(x + 2\pi) = \cos x .
> $$
>
> The tangent function $\tan x = \dfrac{\sin x}{\cos x}$ is undefined where $\cos x = 0$, that is, at $x = \pm\pi/2, \pm 3\pi/2, \ldots$. Its range is $(-\infty, \infty)$, and it has period $\pi$:
>
> $$
> \tan(x + \pi) = \tan x \quad \text{for all } x \text{ in its domain} .
> $$
>
> The remaining trigonometric functions, cosecant, secant and cotangent, are the reciprocals of sine, cosine and tangent: $\csc x = 1/\sin x$, $\sec x = 1/\cos x$, $\cot x = 1/\tan x$.
>
> *Stewart: 1.2 (boxed; tangent in the text)*

^thm-2-4

> [!proof]+ Proof
> Stewart states these facts without proof (Appendix D). From the definitions: the angles $x$ and $x + 2\pi$ differ by one full turn, so they have the same terminal side, hence the same point $(a, b)$ and the same sine and cosine.
>
> The angle $x + \pi$ differs from $x$ by a half turn, so its terminal side is the opposite ray, which contains $(-a, -b)$ at the same distance $r$. Hence $\sin(x + \pi) = -\sin x$ and $\cos(x + \pi) = -\cos x$, and
>
> $$
> \tan(x + \pi) = \frac{-\sin x}{-\cos x} = \tan x .
> $$
>
> Since $\cos(x + \pi) = -\cos x$, the points $x + \pi$ and $x$ lie in the domain of $\tan$ together.
>
> For the range: given any real number $t$, the angle $x$ in $(-\pi/2, \pi/2)$ whose terminal side passes through $(1, t)$ has $\tan x = t/1 = t$.

^pf-2-4

*Uses:* [[§119 Trigonometry#^def-119-4|Def. §119.4]]; the $2\pi$-periodicity is also [[§119 Trigonometry#^thm-119-5|Theorem §119.5]]

The periodicity makes sine and cosine suitable for modeling repetitive phenomena such as tides, vibrating springs and sound waves. In [[§3 New Functions from Old Functions#^ex-3-3|Ex. §3.3]] the number of hours of daylight in Philadelphia $t$ days after January 1 is modeled by $L(t) = 12 + 2.8 \sin\big[\frac{2\pi}{365}(t - 80)\big]$.

> [!example] Example §2.4: The Domain of a Trigonometric Expression
> Find the domain of $f(x) = \dfrac{1}{1 - 2\cos x}$.
>
> $f(x)$ is defined except where the denominator is $0$:
>
> $$
> 1 - 2\cos x = 0 \iff \cos x = \tfrac12 \iff x = \frac{\pi}{3} + 2n\pi \ \text{ or } \ x = \frac{5\pi}{3} + 2n\pi ,
> $$
>
> where $n$ is any integer. (In $[0, 2\pi)$, $\cos x = \frac12$ exactly at $\pi/3$ and $5\pi/3$; by periodicity, [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^thm-2-4|Theorem §2.4]], adding any multiple of $2\pi$ gives all solutions.) So the domain is the set of all real numbers except $\frac{\pi}{3} + 2n\pi$ and $\frac{5\pi}{3} + 2n\pi$, $n \in \mathbb{Z}$.
>
> *Stewart: Example 1.2.5*

^ex-2-4

## Exponential Functions

> [!definition] Definition §2.10: Exponential Function
> The **exponential functions** are the functions $f(x) = b^x$, where the base $b$ is a positive constant. For $b \ne 1$ the domain is $(-\infty, \infty)$ and the range is $(0, \infty)$. The graph rises from left to right if $b > 1$ (for example $y = 2^x$) and falls if $b < 1$ (for example $y = (0.5)^x$); both pass through $(0, 1)$. Exponential functions model growth (if $b > 1$) and decline (if $b < 1$), for instance of populations. They are studied in detail in [[§4 Exponential Functions|§4]].
>
> *Stewart: 1.2 (text)*

^def-2-10

## Logarithmic Functions

> [!definition] Definition §2.11: Logarithmic Function
> The **logarithmic functions** are the functions $f(x) = \log_b x$, where the base $b$ is a positive constant ($b \ne 1$). They are the inverse functions of the exponential functions ([[§5 Inverse Functions and Logarithms#^def-5-3|Definition §5.3]]). The domain is $(0, \infty)$ and the range is $(-\infty, \infty)$. For $b > 1$ the graph passes through $(1, 0)$, and the function increases slowly when $x > 1$, the more slowly the larger the base ($\log_2 x$, $\log_3 x$, $\log_5 x$, $\log_{10} x$).
>
> *Stewart: 1.2 (text)*

^def-2-11

> [!example] Example §2.5: Classifying Functions
> Classify each function as one of the types above: (a) $f(x) = 5^x$, (b) $g(x) = x^5$, (c) $h(x) = \dfrac{1 + x}{1 - \sqrt{x}}$, (d) $u(t) = 1 - t + 5t^4$.
>
> **(a)** $5^x$ is an exponential function: the variable is the *exponent*.
>
> **(b)** $x^5$ is a power function: the variable is the *base*. It is also a polynomial of degree $5$.
>
> **(c)** $h$ is an algebraic function, built from polynomials by division and a square root. It is not rational, because the denominator $1 - \sqrt{x}$ is not a polynomial.
>
> **(d)** $u(t) = 1 - t + 5t^4$ is a polynomial of degree $4$.
>
> *Stewart: Example 1.2.6*

^ex-2-5

> [!remark] Remark: The Essential Functions at a Glance
> | family | formula | domain | shape of the graph |
> |---|---|---|---|
> | linear | $mx + b$ | $\mathbb{R}$ | line of slope $m$; horizontal if $m = 0$ |
> | power, $n$ even | $x^n$ | $\mathbb{R}$ | U-shaped, symmetric about the $y$-axis |
> | power, $n$ odd | $x^n$ | $\mathbb{R}$ | rising, symmetric about the origin |
> | root, $n$ even | $\sqrt[n]{x}$ | $[0, \infty)$ | rising from $(0, 0)$, ever more slowly |
> | root, $n$ odd | $\sqrt[n]{x}$ | $\mathbb{R}$ | rising, vertical tangent at $0$, symmetric about the origin |
> | reciprocal | $1/x^n$ | $x \ne 0$ | two branches, asymptotes the coordinate axes; odd $n$: symmetric about the origin, even $n$: both branches above the $x$-axis |
> | exponential | $b^x$ | $\mathbb{R}$ | through $(0, 1)$, above the $x$-axis; rising if $b > 1$, falling if $b < 1$ |
> | logarithmic | $\log_b x$ | $(0, \infty)$ | through $(1, 0)$; rising slowly if $b > 1$ |
> | sine, cosine | $\sin x$, $\cos x$ | $\mathbb{R}$ | waves between $-1$ and $1$, period $2\pi$ |
> | tangent | $\tan x$ | $x \ne \frac{\pi}{2} + n\pi$ | rising branches between vertical asymptotes, period $\pi$ |
>
> (A summary of Stewart's Table 3.)

^rem-2-2
