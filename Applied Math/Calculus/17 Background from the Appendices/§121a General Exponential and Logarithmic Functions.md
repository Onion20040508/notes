---
type: section
subject: "[[Calculus]]"
chapter: 17
section: "121a"
stewart: "Appendix G"
aliases: ["Stewart Appendix G (cont.)"]
tags: [calculus]
---
← [[§121 The Logarithm Defined as an Integral]] · ↑ [[· 17 Background from the Appendices]]

*Stewart, Appendix G.*

With $\ln x$ *defined* as $\int_1^x dt/t$ ([[§121 The Logarithm Defined as an Integral#^def-121-1|Definition §121.1]]) and $e^x$ as its inverse ([[§121 The Logarithm Defined as an Integral#^def-121-3|Definition §121.3]], [[§121 The Logarithm Defined as an Integral#^def-121-4|Definition §121.4]]), $b^x$ and $\log_b x$ are defined from these. Every law of logarithms and exponents and every differentiation formula is then proved, and the new definitions agree with the old ones ([[§121 The Logarithm Defined as an Integral#^thm-121-12|Theorem §121.12]] and [[§121 The Logarithm Defined as an Integral#^rem-121-2|the closing remark]]).

## General Exponential Functions

> [!definition] Definition §121.5: Exponential Function with Base b
> For $b > 0$ and $r$ rational, (9) and Law 3 of [[§121 The Logarithm Defined as an Integral#^thm-121-6|Theorem §121.6]] give $b^r = (e^{\ln b})^r = e^{r\ln b}$. Therefore, for every real number $x$, *define*
>
> $$
> b^x = e^{x\ln b} . \qquad (13)
> $$
>
> The function $f(x) = b^x$ is the **exponential function with base $b$**. It is positive for all $x$, because $e^x$ is. With $b = e$, (13) gives $e^{x \ln e} = e^x$, consistent with [[§121 The Logarithm Defined as an Integral#^def-121-4|Definition §121.4]].
>
> *Stewart: Appendix G, Definition 13*

^def-121-5

> [!remark]- Connections
> - Complex-variables version: [[§35 The Power Function#^def-35-3|342 Def. §35.3]] ($c^z = e^{z\log c}$, multiple-valued in general) and [[§35 The Power Function#^def-35-1|342 Def. §35.1]] (the power function $z^c = e^{c\log z}$).

> [!example] Example §121.2: An Irrational Power
> By (13), $2^{\sqrt3} = e^{\sqrt3\ln 2}$. Here $\sqrt3\ln 2 \approx 1.7321 \times 0.6931 \approx 1.2006$, so $2^{\sqrt3} \approx e^{1.20} \approx 3.32$.
>
> *Stewart: Appendix G (text)*

^ex-121-2

> [!theorem] Theorem §121.8: The Logarithm of a Power
> $$
> \ln(b^r) = r\ln b \qquad \text{for any real number } r \text{ and } b > 0 . \qquad (14)
> $$
>
> This extends Law 3 of [[§121 The Logarithm Defined as an Integral#^thm-121-2|Theorem §121.2]] from rational to real exponents.
>
> *Stewart: Appendix G, Equation 14*

^thm-121-8

> [!proof]+ Proof
> By Definition 13 and (10), $\ln(b^r) = \ln(e^{r\ln b}) = r\ln b$.

^pf-121-8

*Uses:* [[§121 The Logarithm Defined as an Integral#^def-121-5|Def. §121.5]], [[§121 The Logarithm Defined as an Integral#^def-121-4|Def. §121.4]]

> [!theorem] Theorem §121.9: Laws of Exponents
> If $x$ and $y$ are real numbers and $a, b > 0$, then
>
> $$
> 1.\ b^{x + y} = b^xb^y \qquad 2.\ b^{x - y} = \frac{b^x}{b^y} \qquad 3.\ (b^x)^y = b^{xy} \qquad 4.\ (ab)^x = a^xb^x
> $$
>
> *Stewart: Appendix G, (15) Laws of Exponents*

^thm-121-9

> [!proof]+ Proof
> **Law 1.** By Definition 13 and Law 1 of [[§121 The Logarithm Defined as an Integral#^thm-121-6|Theorem §121.6]],
>
> $$
> b^{x + y} = e^{(x + y)\ln b} = e^{x\ln b + y\ln b} = e^{x\ln b}e^{y\ln b} = b^xb^y .
> $$
>
> **Law 2** (Stewart's Exercise 8). $b^{x - y} = e^{x\ln b - y\ln b} = \dfrac{e^{x\ln b}}{e^{y\ln b}} = \dfrac{b^x}{b^y}$, by Law 2 of [[§121 The Logarithm Defined as an Integral#^thm-121-6|Theorem §121.6]].
>
> **Law 3.** By (14), $\ln(b^x) = x\ln b$, so
>
> $$
> (b^x)^y = e^{y\ln(b^x)} = e^{yx\ln b} = e^{xy\ln b} = b^{xy} .
> $$
>
> **Law 4** (Stewart's Exercise 9). By Law 1 of logarithms, $\ln(ab) = \ln a + \ln b$, so $(ab)^x = e^{x\ln(ab)} = e^{x\ln a + x\ln b} = e^{x\ln a}e^{x\ln b} = a^xb^x$.
>
> In particular Law 3 with $b = e$ gives $(e^x)^r = e^{rx}$ for every real $r$.

^pf-121-9

*Uses:* [[§121 The Logarithm Defined as an Integral#^def-121-5|Def. §121.5]], [[§121 The Logarithm Defined as an Integral#^thm-121-6|§121.6]], [[§121 The Logarithm Defined as an Integral#^thm-121-8|§121.8]], [[§121 The Logarithm Defined as an Integral#^thm-121-2|§121.2]]

> [!theorem] Theorem §121.10: Derivative of b^x
> $$
> \frac{d}{dx}(b^x) = b^x\ln b . \qquad (16)
> $$
>
> So if $b > 1$, then $\ln b > 0$ and $y = b^x$ is increasing; if $0 < b < 1$, then $\ln b < 0$ and $y = b^x$ is decreasing.
>
> *Stewart: Appendix G, Equation 16*

^thm-121-10

> [!proof]+ Proof
> By Definition 13, [[§121 The Logarithm Defined as an Integral#^thm-121-7|Theorem §121.7]] and the Chain Rule,
>
> $$
> \frac{d}{dx}(b^x) = \frac{d}{dx}\big(e^{x\ln b}\big) = e^{x\ln b}\,\frac{d}{dx}(x\ln b) = b^x\ln b .
> $$
>
> Since $b^x > 0$, the sign of the derivative is the sign of $\ln b$, which is positive for $b > 1$ and negative for $0 < b < 1$ ($\ln$ is increasing with $\ln 1 = 0$). The monotonicity follows from the Increasing/Decreasing Test ([[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Theorem §27.1]]).

^pf-121-10

*Uses:* [[§121 The Logarithm Defined as an Integral#^def-121-5|Def. §121.5]], [[§121 The Logarithm Defined as an Integral#^thm-121-7|§121.7]], [[§121 The Logarithm Defined as an Integral#^thm-121-3|§121.3]], [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|§27.1]]

## General Logarithmic Functions

> [!definition] Definition §121.6: Logarithm with Base b
> If $b > 0$ and $b \ne 1$, then $f(x) = b^x$ is one-to-one ([[§121a General Exponential and Logarithmic Functions#^thm-121-10|Theorem §121.10]]). Its inverse function is the **logarithmic function with base $b$**, denoted $\log_b$:
>
> $$
> \log_b x = y \iff b^y = x . \qquad (17)
> $$
>
> In particular $\log_e x = \ln x$.
>
> *Stewart: Appendix G, Equation 17*

^def-121-6

> [!theorem] Theorem §121.11: Change of Base and the Derivative of log_b
> For $b > 0$, $b \ne 1$ and $x > 0$,
>
> $$
> \log_b x = \frac{\ln x}{\ln b}, \qquad \frac{d}{dx}(\log_b x) = \frac{1}{x\ln b} . \qquad (18)
> $$
>
> Moreover $\log_b(xy) = \log_b x + \log_b y$, $\log_b(x/y) = \log_b x - \log_b y$ and $\log_b(x^y) = y\log_b x$ for $x, y > 0$ (in the last, $y$ any real number).
>
> *Stewart: Appendix G, Equation 18 (laws: Exercise 10)*

^thm-121-11

> [!proof]+ Proof
> Let $y = \log_b x$, so $b^y = x$. Taking $\ln$ and using (14), $y\ln b = \ln x$, and $\ln b \ne 0$ because $b \ne 1$. So $\log_b x = y = \dfrac{\ln x}{\ln b}$. Since $\ln b$ is a constant, [[§121 The Logarithm Defined as an Integral#^thm-121-1|Theorem §121.1]] gives
>
> $$
> \frac{d}{dx}(\log_b x) = \frac{1}{\ln b}\,\frac{d}{dx}(\ln x) = \frac{1}{x\ln b} .
> $$
>
> The laws (Stewart's Exercise 10 asks to deduce them from the laws of exponents) follow by dividing the laws of logarithms by $\ln b$: $\log_b(xy) = \frac{\ln x + \ln y}{\ln b}$, $\log_b\frac xy = \frac{\ln x - \ln y}{\ln b}$, and, by (14), $\log_b(x^y) = \frac{y\ln x}{\ln b}$.

^pf-121-11

*Uses:* [[§121 The Logarithm Defined as an Integral#^def-121-6|Def. §121.6]], [[§121 The Logarithm Defined as an Integral#^thm-121-8|§121.8]], [[§121 The Logarithm Defined as an Integral#^thm-121-1|§121.1]], [[§121 The Logarithm Defined as an Integral#^thm-121-2|§121.2]]

## The Number e as a Limit

> [!theorem] Theorem §121.12: e as a Limit
> $$
> e = \lim_{x \to 0} (1 + x)^{1/x} . \qquad (19)
> $$
>
> So the number $e$ of [[§121 The Logarithm Defined as an Integral#^def-121-2|Definition §121.2]] is the number $e$ of Section 3.1 ([[§14 Derivatives of Polynomials and Exponential Functions#^def-14-2|Definition §14.2]]) and of Equation 3.6.5 ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Theorem §19.7]]).
>
> *Stewart: Appendix G, Theorem 19*

^thm-121-12

> [!proof]+ Proof
> Let $f(x) = \ln x$. Then $f'(x) = 1/x$, so $f'(1) = 1$. By the definition of the derivative,
>
> $$
> f'(1) = \lim_{h \to 0} \frac{f(1 + h) - f(1)}{h} = \lim_{x \to 0} \frac{\ln(1 + x) - \ln 1}{x} = \lim_{x \to 0} \frac1x\ln(1 + x) = \lim_{x \to 0} \ln(1 + x)^{1/x} ,
> $$
>
> using $\ln 1 = 0$ and (14) (for $-1 < x$, $x \ne 0$, so that $1 + x > 0$). Because $f'(1) = 1$, $\lim_{x \to 0} \ln(1 + x)^{1/x} = 1$. Since $\exp$ is continuous ([[§121 The Logarithm Defined as an Integral#^thm-121-5|Theorem §121.5]]), Theorem 2.5.8 ([[§10 Continuity#^thm-10-7|Theorem §10.7]]) lets the limit pass inside it, and by (9)
>
> $$
> e = e^1 = e^{\lim_{x \to 0} \ln(1 + x)^{1/x}} = \lim_{x \to 0} e^{\ln(1 + x)^{1/x}} = \lim_{x \to 0} (1 + x)^{1/x} .
> $$

^pf-121-12

*Uses:* [[§121 The Logarithm Defined as an Integral#^thm-121-1|§121.1]], [[§121 The Logarithm Defined as an Integral#^thm-121-8|§121.8]], [[§121 The Logarithm Defined as an Integral#^thm-121-5|§121.5]], [[§121 The Logarithm Defined as an Integral#^def-121-4|Def. §121.4]], [[§10 Continuity#^thm-10-7|§10.7]] (limit of a composite function), [[§12 Derivatives and Rates of Change#^def-12-3|Def. §12.3]] (definition of the derivative)

## Agreement with the Earlier Definitions

> [!remark]- Remark: Dictionary with Chapters 1 and 3
> Each function and formula of Chapters 1 and 3 and its rigorous counterpart here:
>
> | | Chapters 1 and 3 | Appendix G |
> |---|---|---|
> | $\ln x$ | [[§5 Inverse Functions and Logarithms#^def-5-4\|Def. §5.4]] ($\log_e$) | [[§121 The Logarithm Defined as an Integral#^def-121-1\|Def. §121.1]]; $\log_e = \ln$ by [[§121 The Logarithm Defined as an Integral#^def-121-6\|Def. §121.6]] |
> | $e$ | [[§4 Exponential Functions#^def-4-4\|Def. §4.4]], [[§14 Derivatives of Polynomials and Exponential Functions#^def-14-2\|Def. §14.2]] | [[§121 The Logarithm Defined as an Integral#^def-121-2\|Def. §121.2]]; the same number by [[§121 The Logarithm Defined as an Integral#^thm-121-12\|Thm. §121.12]] and [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7\|Thm. §19.7]] |
> | $e^x$, $b^x$ | [[§4 Exponential Functions#^def-4-2\|Def. §4.2]], [[§4 Exponential Functions#^def-4-3\|Def. §4.3]] | [[§121 The Logarithm Defined as an Integral#^def-121-4\|Def. §121.4]], [[§121 The Logarithm Defined as an Integral#^def-121-5\|Def. §121.5]]; equal for rational $x$ by [[§121 The Logarithm Defined as an Integral#^prop-121-4\|Prop. §121.4]], for irrational $x$ see below |
> | $\log_b x$ | [[§5 Inverse Functions and Logarithms#^def-5-3\|Def. §5.3]] | [[§121 The Logarithm Defined as an Integral#^def-121-6\|Def. §121.6]] |
> | inverse pair $\ln$, $e^x$ | [[§5 Inverse Functions and Logarithms#^cor-5-6\|Cor. §5.6]] | (8)–(10) of [[§121 The Logarithm Defined as an Integral#^def-121-4\|Def. §121.4]] |
> | laws of exponents | [[§4 Exponential Functions#^thm-4-1\|Thm. §4.1]] | [[§121 The Logarithm Defined as an Integral#^thm-121-6\|Thm. §121.6]], [[§121 The Logarithm Defined as an Integral#^thm-121-9\|Thm. §121.9]] |
> | laws of logarithms, change of base | [[§5 Inverse Functions and Logarithms#^thm-5-5\|Thm. §5.5]], [[§5 Inverse Functions and Logarithms#^thm-5-8\|Thm. §5.8]] | [[§121 The Logarithm Defined as an Integral#^thm-121-2\|Thm. §121.2]], [[§121 The Logarithm Defined as an Integral#^thm-121-8\|Thm. §121.8]], [[§121 The Logarithm Defined as an Integral#^thm-121-11\|Thm. §121.11]] |
> | $(\ln x)' = 1/x$ | [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3\|Cor. §19.3]] | [[§121 The Logarithm Defined as an Integral#^thm-121-1\|Thm. §121.1]] |
> | $(e^x)' = e^x$ | [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6\|Thm. §14.6]] | [[§121 The Logarithm Defined as an Integral#^thm-121-7\|Thm. §121.7]] |
> | $(b^x)' = b^x\ln b$ | [[§17 The Chain Rule#^thm-17-5\|Thm. §17.5]] | [[§121 The Logarithm Defined as an Integral#^thm-121-10\|Thm. §121.10]] |
> | $(\log_b x)' = 1/(x\ln b)$ | [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-2\|Thm. §19.2]] | [[§121 The Logarithm Defined as an Integral#^thm-121-11\|Thm. §121.11]] |
>
> **Irrational exponents agree.** Let $b > 1$ and $x$ irrational. For rationals $r < x < s$, the function $t \mapsto e^{t\ln b}$ is increasing ([[§121a General Exponential and Logarithmic Functions#^thm-121-10|Theorem §121.10]]) and equals $b^t$ at rational $t$ (by (9) and Law 3 of [[§121 The Logarithm Defined as an Integral#^thm-121-6|Theorem §121.6]], as in [[§121a General Exponential and Logarithmic Functions#^def-121-5|Definition §121.5]]), so $b^r < e^{x\ln b} < b^s$. Thus $e^{x\ln b}$ is the unique number between all $b^r$ and all $b^s$ that [[§4 Exponential Functions#^def-4-3|Definition §4.3]] calls $b^x$; for $0 < b < 1$ reverse the inequalities, and $1^x = e^0 = 1$. So every result proved here is a proof of the corresponding statement taken on credit earlier.

^rem-121-2
