---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 6
bdp: "2.3"
aliases: ["BDP 2.3"]
tags: [ordinary-differential-equations, math331]
---
← [[§5 Separable Differential Equations]] · ↑ [[· 2 First-Order Differential Equations]] · [[§7 Differences Between Linear and Nonlinear Differential Equations]] →

*Boyce–DiPrima, Section 2.3 · MATH 331 Written HW 1 (Problem 4), Written HW 2 (Problems 1 and 3), Midterm Fall 2021 (Q6).*

This section applies the methods of [[§4 Linear Differential Equations; Method of Integrating Factors|§4]] and [[§5 Separable Differential Equations|§5]] to typical models: mixing in a tank or pond, investments with continuous interest and deposits, cooling, and a body launched away from the earth. Each problem goes through the same three steps: translate the physical situation into a differential equation, analyze that equation, and check the results against reality. The mixing and finance models are linear, so the integrating factor solves them completely, including a pond whose inflow varies periodically. The launch problem is nonlinear, but becomes separable once the altitude replaces time as the independent variable, and gives the escape velocity $\sqrt{2gR}$.

## The Modeling Process

> [!remark] Remark: Method — The Three Steps of Mathematical Modeling
> 1. **Construction of the model.** Translate the physical situation into mathematical terms, using the steps of [[§1 Some Basic Mathematical Models; Direction Fields#^rem-1-3|Remark: Method — Constructing a Mathematical Model]]. Most critical is to state clearly the principles believed to govern the process (heat flows at a rate proportional to the temperature difference; Newton's laws; populations grow at a rate proportional to their size). Each involves a rate of change, so it leads to a differential equation. The model is almost always only an approximate description of the real process, or an exact description of a simplified one. It may replace a discrete process (a population changing by whole numbers) by a continuous one.
> 2. **Analysis of the model.** Solve the equation, or find out as much as possible about its solutions. If this is too hard, further approximations may be made: a nonlinear equation replaced by a linear one, a slowly varying coefficient by a constant. Such approximations must also be checked physically.
> 3. **Comparison with experiment or observation.** Interpret the solution in the original context. Check that it is physically reasonable, compare computed values with observed ones, examine the behavior after a long time and for special values of the parameters. Agreement does not prove the model correct, but serious disagreement means an error in the solution, a model that needs refinement, or observations that need more care.

^rem-6-1

## Mixing

> [!remark] Remark: Method — Mixing Problems
> Let $Q(t)$ be the amount of a substance (salt, a chemical) dissolved in a tank, assumed **well stirred**, so that the concentration is uniform: $Q(t)/V(t)$, where $V(t)$ is the volume of liquid.
> 1. **Balance law.** If the substance is neither created nor destroyed in the tank,
>
> $$
> \frac{dQ}{dt} = \text{rate in} - \text{rate out} . \qquad (1)
> $$
>
> 2. **Rate in** $=$ (concentration of the inflow) $\times$ (inflow rate).
> 3. **Rate out** $=$ $\dfrac{Q(t)}{V(t)} \times$ (outflow rate).
> 4. **Volume.** With constant flow rates, $V(t) = V_0 + (r_{\text{in}} - r_{\text{out}})\,t$. If the rates are equal, $V$ is constant; otherwise the model holds only until the tank overflows or empties.
> 5. **Solve.** The result is the linear equation $Q' + \dfrac{r_{\text{out}}}{V(t)}\,Q = (\text{rate in})$; use the integrating factor ([[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|Theorem §4.2]]). The limiting amount, if there is one, can be found by setting $dQ/dt = 0$.
>
> Stewart's version, with constant volume: [[§59 Separable Equations#^rem-59-4|Calc Remark: Method — Mixing Problems]].

^rem-6-2

> [!example] Example §6.1: A Tank at Constant Volume
> At $t = 0$ a tank contains $Q_0$ lb of salt dissolved in $100$ gal of water. Water containing $\frac14$ lb of salt per gallon enters at $r$ gal/min, and the well-stirred mixture drains at the same rate. Find $Q(t)$ and the limiting amount $Q_L$. If $r = 3$ and $Q_0 = 2Q_L$, find the time $T$ after which the salt level is within $2\%$ of $Q_L$. What flow rate makes $T \le 45$ min?
>
> **Model.** The rate in is $\frac14 \cdot r = \frac r4$ lb/min. The volume stays $100$ gal, so the concentration is $Q/100$ and the rate out is $\frac{rQ}{100}$ lb/min. Hence
>
> $$
> \frac{dQ}{dt} = \frac r4 - \frac{rQ}{100} , \qquad Q(0) = Q_0 . \qquad (2), (3)
> $$
>
> **Limiting amount.** Physically, the original mixture is eventually replaced by the inflow, of concentration $\frac14$ lb/gal, so we expect about $25$ lb. Indeed $dQ/dt = 0$ gives $Q_L = 25$.
>
> **Solve.** In standard form $Q' + \frac{r}{100}Q = \frac r4$; the integrating factor is $e^{rt/100}$, and $(e^{rt/100}Q)' = \frac r4 e^{rt/100}$ gives $e^{rt/100}Q = 25e^{rt/100} + c$, so $Q = 25 + ce^{-rt/100}$. The initial condition gives $c = Q_0 - 25$:
>
> $$
> Q(t) = 25 + (Q_0 - 25)e^{-rt/100} = 25\big(1 - e^{-rt/100}\big) + Q_0e^{-rt/100} . \qquad (6), (7)
> $$
>
> So $Q(t) \to 25$ lb, faster for larger $r$. In the second form, $Q_0e^{-rt/100}$ is the part of the original salt still in the tank, and $25(1 - e^{-rt/100})$ is the salt brought in by the flow. (The equation is also separable.)
>
> **Time to within 2%.** With $r = 3$ and $Q_0 = 50$, $Q(t) = 25 + 25e^{-0.03t}$. Two percent of $25$ is $0.5$, so we need $25e^{-0.03T} = 0.5$, that is, $e^{0.03T} = 50$:
>
> $$
> T = \frac{\ln 50}{0.03} \approx 130.4 \text{ min} .
> $$
>
> **Flow rate for $T = 45$.** Now $25e^{-45r/100} = 0.5$ with $r$ unknown: $\frac{45r}{100} = \ln 50$, so
>
> $$
> r = \frac{100}{45}\ln 50 \approx 8.69 \text{ gal/min} .
> $$
>
> The same model describes a pollutant in a lake or a drug in an organ of the body, where the flow rates may be hard to determine or vary with time, the concentration may be far from uniform, and the inflow and outflow rates may differ ([[§6 Modeling with First-Order Differential Equations#^ex-6-2|Example §6.2]]).
>
> *BDP: Example 2.3.1*

^ex-6-1

> [!example] Example §6.2: Tanks That Fill Up
> **(a)** A $10$ gallon tank contains $5$ gallons of pure water. At $t = 0$ salt water with $\frac12$ lb of salt per gallon flows in at $4$ gal/min, and the well-stirred mixture drains at $3$ gal/min. Set up and solve the initial value problem for the salt $S(t)$, and find the amount of salt when the tank is full.
>
> **Model.** The volume grows by $1$ gal/min: $V(t) = 5 + t$, and the tank is full at $t = 5$. Rate in $= \frac12 \cdot 4 = 2$ lb/min; rate out $= \dfrac{S}{5 + t}\cdot 3$. So
>
> $$
> \frac{dS}{dt} = 2 - \frac{3S}{5 + t} , \qquad S(0) = 0 , \qquad 0 \le t \le 5 .
> $$
>
> **Solve.** $S' + \dfrac{3}{5 + t}S = 2$; the integrating factor is $\mu = e^{3\ln(5 + t)} = (5 + t)^3$. Then $\big((5 + t)^3S\big)' = 2(5 + t)^3$, so $(5 + t)^3S = \frac12(5 + t)^4 + K$. At $t = 0$: $0 = \frac{625}{2} + K$, so $K = -\frac{625}{2}$ and
>
> $$
> S(t) = \frac{5 + t}{2} - \frac{625}{2(5 + t)^3} .
> $$
>
> **When full.** $S(5) = \frac{10}{2} - \frac{625}{2 \cdot 1000} = 5 - \frac{5}{16} = \frac{75}{16} \approx 4.69$ lb, a little less than the $5$ lb that $10$ gallons at the inflow concentration would contain.
>
> **(b)** A $200$ gallon tank initially contains $100$ gallons of pure water. At $t = 0$ water with $c$ lb of salt per gallon enters at $2$ gal/min, and the mixture leaves at $1$ gal/min. Find the salt $Q(t)$ for $0 \le t \le 100$.
>
> **Model.** $V(t) = 100 + t$, reaching $200$ at $t = 100$. Rate in $= 2c$, rate out $= \dfrac{Q}{100 + t}$:
>
> $$
> \frac{dQ}{dt} + \frac{Q}{100 + t} = 2c , \qquad Q(0) = 0 .
> $$
>
> **Solve.** $\mu = e^{\ln(100 + t)} = 100 + t$, so $\big((100 + t)Q\big)' = 2c(100 + t)$ and $(100 + t)Q = 2c\big(100t + \frac{t^2}{2}\big) + K$. At $t = 0$, $K = 0$:
>
> $$
> Q(t) = \frac{2c\big(100t + \frac{t^2}{2}\big)}{100 + t} = \frac{c\,t(200 + t)}{100 + t} , \qquad 0 \le t \le 100 .
> $$
>
> When the tank is full, $Q(100) = \frac{c \cdot 100 \cdot 300}{200} = 150c$ lb, a concentration of $0.75c$ lb/gal.
>
> *Source: 331 Midterm (Fall 2021), Q6*
> *Source: 331 Written HW 1, Problem 4*

^ex-6-2

## Compound Interest

Suppose a sum $S_0$ is deposited at an annual **rate of return** $r$, compounded continuously, and that deposits (or withdrawals) are made continuously at a constant rate $k$ per year ($k > 0$ for deposits, $k < 0$ for withdrawals). The rate of change of the value $S(t)$ is the return $rS$ plus the deposit rate.

> [!theorem] Proposition §6.1: Continuous Compounding with Deposits
> Let $r \ne 0$. The solution of
>
> $$
> \frac{dS}{dt} = rS + k , \qquad S(0) = S_0 \qquad (14), (12)
> $$
>
> is
>
> $$
> S(t) = S_0e^{rt} + \frac kr\big(e^{rt} - 1\big) . \qquad (15)
> $$
>
> The first term is the return on the initial amount, the second the result of the deposits or withdrawals. With $k = 0$ (no deposits), $S(t) = S_0e^{rt}$ (13): the investment grows exponentially.
>
> *BDP: 2.3, Equations (11)–(15)*

^prop-6-1

> [!proof]+ Proof
> In standard form, $\dfrac{dS}{dt} - rS = k$, a linear equation with integrating factor $e^{-rt}$ ([[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-1|Theorem §4.1]] with $a = -r$). Then $(e^{-rt}S)' = ke^{-rt}$, so $e^{-rt}S = -\frac kr e^{-rt} + c$ and
>
> $$
> S(t) = ce^{rt} - \frac kr .
> $$
>
> The initial condition gives $S_0 = c - \frac kr$, so $c = S_0 + \frac kr$, and $S(t) = \big(S_0 + \frac kr\big)e^{rt} - \frac kr$, which is (15). (Equivalently, this is [[§2 Solutions of Some Differential Equations#^thm-2-1|Theorem §2.1]] with $a = r$, $b = -k$.)

^pf-6-1

*Uses:* [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-1|§4.1]], [[§2 Solutions of Some Differential Equations#^thm-2-1|§2.1]]

> [!theorem] Proposition §6.2: Compounding m Times a Year
> If interest at the annual rate $r$ is compounded $m$ times per year, then after $t$ years (with $mt$ a whole number)
>
> $$
> S(t) = S_0\Big(1 + \frac rm\Big)^{mt} , \qquad (17)
> $$
>
> and as the compounding becomes more frequent this tends to the continuously compounded value:
>
> $$
> \lim_{m \to \infty} S_0\Big(1 + \frac rm\Big)^{mt} = S_0e^{rt} .
> $$
>
> *BDP: 2.3, Equation (17) and text*

^prop-6-2

> [!proof]+ Proof
> **Formula (17).** Each period lasts $1/m$ year and multiplies the value by $1 + \frac rm$. Compounded once a year, the value after $t$ years is $S_0(1 + r)^t$; twice a year, it is $S_0(1 + \frac r2)$ after $6$ months, $S_0(1 + \frac r2)^2$ after a year, and $S_0(1 + \frac r2)^{2t}$ after $t$ years. In general there are $mt$ periods in $t$ years, which gives (17).
>
> **The limit.** BDP recalls this from calculus. If $r = 0$ both sides equal $S_0$. If $r \ne 0$, put $h = \frac rm$, so $h \to 0$ as $m \to \infty$ (through positive values if $r > 0$, negative values if $r < 0$, with $|h| < 1$ for large $m$). Then
>
> $$
> \Big(1 + \frac rm\Big)^{mt} = \Big[(1 + h)^{1/h}\Big]^{rt} .
> $$
>
> The inner expression tends to $e$ as $h \to 0$ ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Calc Thm. §19.7]], a two-sided limit), and $u \mapsto u^{rt}$ is continuous at $u = e$, so the value tends to $S_0e^{rt}$.

^pf-6-2

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Calc Thm. §19.7]] ($e$ as a limit)

> [!remark]- Connections
> - See also: [[§21 Exponential Growth and Decay#^cor-21-3|Calc Cor. §21.3]] (Stewart's treatment, with the table of [[§21 Exponential Growth and Decay#^ex-21-4|Calc Ex. §21.4]]) and the limit $\lim_{x \to 0}(1 + x)^{1/x} = e$, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Calc Thm. §19.7]].

> [!remark] Remark: How Much Does the Frequency of Compounding Matter?
> Growth factors $S(t)/S_0$ at $r = 8\%$ (BDP, Table 2.3.1; recomputed):
>
> | years | quarterly, $m = 4$ | daily, $m = 365$ | continuous |
> |---|---|---|---|
> | 1 | 1.0824 | 1.0833 | 1.0833 |
> | 10 | 2.2080 | 2.2253 | 2.2255 |
> | 40 | 23.7699 | 24.5239 | 24.5325 |
>
> The frequency is not particularly important: over $10$ years quarterly and continuous compounding differ by $\$17.50$ per $\$1000$ invested, less than $\$2$ a year. The first row gives the annual yield: $8.24\%$ for quarterly, $8.33\%$ for daily or continuous compounding. Since the same model applies to dividends and capital gains, BDP calls $r$ the rate of return.

^rem-6-3

> [!example] Example §6.3: Saving for Retirement
> **(a) BDP's IRA.** Someone opens a retirement account at age $25$ and invests $\$2000$ a year, continuously, at a rate of return of $8\%$. What is the balance at age $65$?
>
> Here $S_0 = 0$, $r = 0.08$, $k = 2000$, $t = 40$, and (15) gives
>
> $$
> S(40) = \frac{2000}{0.08}\big(e^{3.2} - 1\big) = 25{,}000\big(e^{3.2} - 1\big) \approx \$588{,}313 .
> $$
>
> Only $\$80{,}000$ was invested; the remaining $\$508{,}313$ is accumulated return. The result is sensitive to the rate: $S(40) \approx \$508{,}948$ at $r = 7.5\%$ and $\approx \$681{,}508$ at $r = 8.5\%$.
>
> **(b) Inheritance versus saving.** Two students open retirement accounts at age $22$, both earning a continuous rate of $6\%$, and retire at $65$ (so $t = 43$). Student A deposits an inherited $\$1{,}000{,}000$ at the start and nothing more. Student B starts with $\$0$ and deposits continuously $\$D$ per year. Find $D$ so that both retire with the same amount.
>
> - *Student A:* $k = 0$, so $S_A(43) = 10^6e^{0.06 \cdot 43} = 10^6e^{2.58} \approx \$13{,}197{,}138$.
> - *Student B:* $S_0 = 0$, $k = D$, so $S_B(43) = \dfrac{D}{0.06}\big(e^{2.58} - 1\big)$.
>
> Setting them equal,
>
> $$
> D = \frac{0.06 \cdot 10^6e^{2.58}}{e^{2.58} - 1} = \frac{60{,}000 \cdot 13.1971}{12.1971} \approx \$64{,}919 \text{ per year} .
> $$
>
> Student B deposits about $43 \times \$64{,}919 \approx \$2.79$ million in total to match a single early deposit of $\$1$ million: the early deposit earns return for the full $43$ years.
>
> **Assumptions.** Continuous compounding and continuous deposits are idealizations, and a constant rate of return over decades is not realistic; formula (15) is best used to compare different rate projections. With $r$ and $k$ functions of $t$, the equation is still linear but the solution is more complicated. The same model applies to annuities, mortgages and automobile loans.
>
> *BDP: 2.3 (text)*
> *Source: 331 Written HW 2, Problem 3*

^ex-6-3

## Chemicals in a Pond

> [!example] Example §6.4: A Pond with Periodic Inflow
> A pond initially contains $10$ million gallons of fresh water. Water containing an undesirable chemical flows in at $5$ million gal/yr, and the mixture flows out at the same rate. The concentration of the chemical in the incoming water varies periodically: $\gamma(t) = 2 + \sin 2t$ g/gal. Model the process, find the amount of chemical at any time, and describe the effect of the variation.
>
> **Model.** The volume stays $10^7$ gal. With $Q(t)$ in grams and $t$ in years,
>
> $$
> \text{rate in} = (5 \times 10^6)(2 + \sin 2t) , \qquad \text{rate out} = (5 \times 10^6)\,\frac{Q(t)}{10^7} = \frac{Q(t)}{2} \quad \text{(g/yr)} ,
> $$
>
> so $\dfrac{dQ}{dt} = (5 \times 10^6)(2 + \sin 2t) - \dfrac{Q}{2}$. To make the numbers manageable, let $q(t) = Q(t)/10^6$ (in metric tons); every term then has the factor $10^6$, and
>
> $$
> \frac{dq}{dt} + \frac12 q = 10 + 5\sin 2t , \qquad q(0) = 0 . \qquad (21), (22)
> $$
>
> **Solve.** The coefficient of $q$ is constant, so $\mu = e^{t/2}$ and $(e^{t/2}q)' = 10e^{t/2} + 5e^{t/2}\sin 2t$. Integrating by parts twice (or with the standard formula $\int e^{\alpha t}\sin\beta t\,dt = \frac{e^{\alpha t}(\alpha\sin\beta t - \beta\cos\beta t)}{\alpha^2 + \beta^2}$, here $\alpha = \frac12$, $\beta = 2$, $\alpha^2 + \beta^2 = \frac{17}{4}$),
>
> $$
> \int e^{t/2}\sin 2t\,dt = \frac{4}{17}e^{t/2}\Big(\frac12\sin 2t - 2\cos 2t\Big) = \frac{e^{t/2}}{17}\big(2\sin 2t - 8\cos 2t\big) .
> $$
>
> Hence $e^{t/2}q = 20e^{t/2} + \frac{e^{t/2}}{17}(10\sin 2t - 40\cos 2t) + c$, and
>
> $$
> q(t) = 20 - \frac{40}{17}\cos 2t + \frac{10}{17}\sin 2t + ce^{-t/2} . \qquad (23)
> $$
>
> **Initial condition.** $0 = 20 - \frac{40}{17} + c$, so $c = -\frac{300}{17}$:
>
> $$
> q(t) = 20 - \frac{40}{17}\cos 2t + \frac{10}{17}\sin 2t - \frac{300}{17}e^{-t/2} . \qquad (24)
> $$
>
> **Interpretation.** The exponential term matters for small $t$ but dies out quickly. Afterwards the solution is an oscillation about the level $q = 20$, of amplitude $\sqrt{40^2 + 10^2}/17 = 10/\sqrt{17} \approx 2.43$ tons, with the period $\pi$ of the incoming concentration. Without the $\sin 2t$ term, $q = 20$ would be the equilibrium solution.
>
> **Assumptions.** No water is lost to evaporation or seepage or gained from rain; no chemical is absorbed by organisms in the pond; the concentration is uniform throughout the pond. The accuracy of the results depends strongly on these simplifications.
>
> *BDP: Example 2.3.3*

^ex-6-4

![[m331-6-1.svg]]
*The chemical in the pond, $q(t)$ in metric tons (blue). It equals the steady periodic part $20 - \frac{40}{17}\cos 2t + \frac{10}{17}\sin 2t$ (orange) plus the transient $-\frac{300}{17}e^{-t/2}$, which starts at $-17.6$ and has fallen below $0.1$ in absolute value by $t \approx 10.4$. From then on $q$ oscillates between $20 - 10/\sqrt{17}$ and $20 + 10/\sqrt{17}$ (dotted).*

## Newton's Law of Cooling

> [!example] Example §6.5: Newton's Law of Cooling
> Newton's law of cooling says that the temperature $T(t)$ of an object in a medium at constant temperature $T_m$ changes at a rate proportional to $T - T_m$:
>
> $$
> T' = -k(T - T_m) , \qquad k > 0 ,
> $$
>
> with $k > 0$ because the object cools when $T > T_m$ and warms when $T < T_m$; $k$ is the temperature decay constant. This is $T' = aT - b$ with $a = -k$, $b = -kT_m$, so by [[§2 Solutions of Some Differential Equations#^thm-2-1|Theorem §2.1]] (or by separating variables)
>
> $$
> T(t) = T_m + Ce^{-kt} , \qquad C = T(0) - T_m .
> $$
>
> **(a)** A thermometer is moved from a room at $70$°F to a freezer at $12$°F. After $30$ seconds it reads $40$°F. What does it read after $2$ minutes?
>
> With $t$ in seconds, $T(t) = 12 + 58e^{-kt}$. From $T(30) = 40$: $58e^{-30k} = 28$, so $e^{-30k} = \frac{14}{29}$. Then
>
> $$
> T(120) = 12 + 58\big(e^{-30k}\big)^4 = 12 + 58\Big(\frac{14}{29}\Big)^4 = 12 + \frac{76832}{24389} \approx 12 + 3.15 = 15.15\text{°F} .
> $$
>
> **(b)** An object is placed in a room at $20$°C. Its temperature drops by $5$°C in $4$ minutes and by $7$°C in $8$ minutes. What was its temperature when it was placed in the room?
>
> Here $T(t) = 20 + Ce^{-kt}$ and $T(0) = 20 + C$, so $C$ is the unknown initial excess. The data say $T(0) - T(4) = C(1 - e^{-4k}) = 5$ and $T(0) - T(8) = C(1 - e^{-8k}) = 7$. Put $u = e^{-4k}$, so $e^{-8k} = u^2$:
>
> $$
> C(1 - u) = 5 , \qquad C(1 - u^2) = C(1 - u)(1 + u) = 7 .
> $$
>
> Dividing, $1 + u = \frac75$, so $u = \frac25$ and $C = \frac{5}{1 - 2/5} = \frac{25}{3}$. The initial temperature was
>
> $$
> T(0) = 20 + \frac{25}{3} = \frac{85}{3} \approx 28.3\text{°C} ,
> $$
>
> and $k = \frac14\ln\frac52 \approx 0.229$ per minute. (Check: $T(4) = 20 + \frac{25}{3}\cdot\frac25 = 23\frac13 = T(0) - 5$, and $T(8) = 20 + \frac{25}{3}\cdot\frac{4}{25} = 21\frac13 = T(0) - 7$.)
>
> Stewart's treatment: [[§21 Exponential Growth and Decay#^cor-21-2|Calc Cor. §21.2]].
>
> *Source: 331 Written HW 2, Problem 1*

^ex-6-5

> [!remark]- Connections
> - See also: [[§3★ Boundary Value Problems#^def-3-new1|341 Def. §3.2]] (Newton's law of cooling for the heat a rod loses through its surface) and [[§17 Derivation and Boundary Conditions#^prop-17-3|341 Prop. §17.3]] (at an end of a rod, Newton's law of cooling becomes a Robin boundary condition for the heat equation).

## Escape Velocity

A body of constant mass $m$ is projected away from the earth, perpendicular to its surface, with initial velocity $v_0$. Ignore air resistance, but take into account that gravity weakens with distance. Let the $x$-axis point away from the center of the earth along the line of motion, with $x = 0$ on the surface, and let $R$ be the radius of the earth. The weight is inversely proportional to the square of the distance from the center, $w(x) = -K/(x + R)^2$, and $w(0) = -mg$ gives $K = mgR^2$:

$$
w(x) = -\frac{mgR^2}{(R + x)^2} . \qquad (25)
$$

> [!definition] Definition §6.1: Escape Velocity
> The **escape velocity** $v_e$ is the least initial velocity for which the body does not return to the earth.
>
> *BDP: Example 2.3.4*

^def-6-1

> [!theorem] Proposition §6.3: Velocity, Maximum Altitude and Escape Velocity
> As a function of the altitude $x$, the velocity of the body is
>
> $$
> v = \pm\sqrt{v_0^2 - 2gR + \frac{2gR^2}{R + x}} , \qquad (30)
> $$
>
> with the plus sign while it rises and the minus sign while it falls back. If $v_0 < \sqrt{2gR}$, the body reaches the maximum altitude
>
> $$
> A_{\max} = \frac{v_0^2R}{2gR - v_0^2} ; \qquad (31)
> $$
>
> to reach a given altitude $A_{\max}$ it needs the initial velocity
>
> $$
> v_0 = \sqrt{2gR\,\frac{A_{\max}}{R + A_{\max}}} . \qquad (32)
> $$
>
> The escape velocity is
>
> $$
> v_e = \sqrt{2gR} , \qquad (33)
> $$
>
> approximately $11.2$ km/s, or about $6.95$ mi/s.
>
> *BDP: Example 2.3.4*

^prop-6-3

> [!proof]+ Proof
> **The equation.** The only force is (25), so Newton's second law and the initial condition give
>
> $$
> m\,\frac{dv}{dt} = -\frac{mgR^2}{(R + x)^2} , \qquad v(0) = v_0 . \qquad (26), (27)
> $$
>
> This involves too many variables: $t$, $x$ and $v$. Eliminate $t$ by taking $x$ as the independent variable. While the body rises, $x$ is a strictly increasing function of $t$, so $t$, and with it $v$, can be regarded as a function of $x$ (BDP does this without comment; this is why). By the chain rule,
>
> $$
> \frac{dv}{dt} = \frac{dv}{dx}\,\frac{dx}{dt} = v\,\frac{dv}{dx} , \qquad\text{so}\qquad v\,\frac{dv}{dx} = -\frac{gR^2}{(R + x)^2} . \qquad (28)
> $$
>
> **Solve.** Equation (28) is separable but not linear. Separating and integrating ([[§5 Separable Differential Equations#^thm-5-1|Theorem §5.1]]),
>
> $$
> \frac{v^2}{2} = \frac{gR^2}{R + x} + c . \qquad (29)
> $$
>
> At $t = 0$ we have $x = 0$, so the initial condition becomes $v = v_0$ at $x = 0$: $c = \frac{v_0^2}{2} - gR$. Hence $v^2 = v_0^2 - 2gR + \frac{2gR^2}{R + x}$, which is (30). (The same relation holds on the way down, where $x$ is decreasing in $t$, by the same argument; it is conservation of energy.)
>
> **Maximum altitude.** At the highest point $v = 0$ and $x = A_{\max}$:
>
> $$
> \frac{2gR^2}{R + A_{\max}} = 2gR - v_0^2 , \qquad A_{\max} = \frac{2gR^2}{2gR - v_0^2} - R = \frac{v_0^2R}{2gR - v_0^2} ,
> $$
>
> which is (31); it requires $v_0^2 < 2gR$. Solving (31) for $v_0$: $v_0^2(R + A_{\max}) = 2gRA_{\max}$, which gives (32).
>
> **Escape velocity.** As $A_{\max} \to \infty$, $\frac{A_{\max}}{R + A_{\max}} \to 1$ and (32) tends to $\sqrt{2gR}$. To see that this is the least velocity for which the body never returns (BDP takes the limit without comment): if $v_0 \ge \sqrt{2gR}$, then $v^2 = (v_0^2 - 2gR) + \frac{2gR^2}{R + x} > 0$ for every $x \ge 0$, so $v$ never vanishes, stays positive, and the body never turns back. If $v_0 < \sqrt{2gR}$, then $v^2$ decreases to $0$ at the finite altitude (31), where the body stops and falls back. So $v_e = \sqrt{2gR}$.
>
> **Numbers.** With $g \approx 9.8$ m/s² and $R \approx 6.37 \times 10^6$ m, $\sqrt{2gR} \approx 1.12 \times 10^4$ m/s $\approx 11.2$ km/s; with $g \approx 32.2$ ft/s² and $R \approx 3960$ mi, about $6.95$ mi/s.

^pf-6-3

*Uses:* [[§5 Separable Differential Equations#^thm-5-1|§5.1]], [[§6 Modeling with First-Order Differential Equations#^def-6-1|Def. §6.1]]

> [!remark] Remark: Limits of the Escape-Velocity Model
> The calculation neglects air resistance, so the actual escape velocity is somewhat higher. On the other hand, launching from a considerable height above sea level reduces it, since both gravity and air resistance (which falls off rapidly with altitude) are then smaller. Also, imparting a large velocity instantaneously may be impractical; space vehicles receive their initial acceleration over several minutes.

^rem-6-4
