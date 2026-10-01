---
type: section
subject: "[[Calculus]]"
chapter: 9
section: 60
stewart: "9.4"
aliases: ["Stewart 9.4"]
tags: [calculus]
---
← [[§59 Separable Equations]] · ↑ [[· 9 Differential Equations]] · [[§61 Linear Equations]] →

*Stewart, Section 9.4.*

[[§57 Modeling with Differential Equations|§57]] set up two differential equations for a population: the law of natural growth $dP/dt = kP$ and the logistic equation $dP/dt = kP(1 - P/M)$. Both are separable, so the method of [[§59 Separable Equations|§59]] solves them explicitly. Natural growth gives exponential functions. The logistic equation gives S-shaped curves that level off at the carrying capacity $M$ and grow fastest at $M/2$. Fitted to the same data, the logistic model is much more accurate once the population is no longer small. The section ends with variants for harvesting and for a minimum viable population.

## The Law of Natural Growth

Why should a population grow at a rate proportional to its size? Suppose $1000$ bacteria grow at a rate of $P' = 300$ bacteria per hour. Add another $1000$ bacteria of the same type. Each half of the combined population grows at $300$ per hour, so the population of $2000$ grows at $600$ per hour, at least initially (provided there is enough room and nutrition). Doubling the size doubles the growth rate.

> [!definition] Definition §60.1: Law of Natural Growth
> If $P(t)$ is the value of a quantity at time $t$ and the rate of change of $P$ with respect to $t$ is proportional to its size $P(t)$ at any time, then
>
> $$
> \frac{dP}{dt} = kP \qquad (1)
> $$
>
> for a constant $k$. Equation 1 is the **law of natural growth**. If $k > 0$ the population increases; if $k < 0$ it decreases. Equivalently,
>
> $$
> \frac{dP/dt}{P} = k :
> $$
>
> the **relative growth rate** (the growth rate divided by the population size; [[§21 Exponential Growth and Decay#^def-21-2|Definition §21.2]]) is constant.
>
> *Stewart: 9.4, Equation 1*

^def-60-1

> [!theorem] Theorem §60.1: Solution of the Natural Growth Equation
> The solution of the initial-value problem
>
> $$
> \frac{dP}{dt} = kP, \qquad P(0) = P_0
> $$
>
> is
>
> $$
> P(t) = P_0\,e^{kt} .
> $$
>
> So a population with constant relative growth rate grows exponentially. This is [[§21 Exponential Growth and Decay#^thm-21-1|Theorem §21.1]] (Stewart 3.8, Theorem 2), where it is applied to populations, radioactive decay, Newton's law of cooling and compound interest.
>
> *Stewart: 9.4, Equation 2*

^thm-60-1

> [!proof]+ Proof
> Equation 1 is separable ([[§59 Separable Equations#^def-59-1|Definition §59.1]]). The constant function $P = 0$ is a solution. Where $P \ne 0$,
>
> $$
> \int \frac{dP}{P} = \int k\,dt \qquad\Longrightarrow\qquad \ln|P| = kt + C \qquad\Longrightarrow\qquad |P| = e^{kt + C} = e^{C} e^{kt} ,
> $$
>
> so $P = A\,e^{kt}$, where $A$ ($= \pm e^{C}$ or $0$) is an arbitrary constant. To see what $A$ means, put $t = 0$: $P(0) = A\,e^{k \cdot 0} = A$. So $A$ is the initial value $P_0$, and $P(t) = P_0\,e^{kt}$.
>
> **Every solution.** The computation divides by $P$, so it finds only the zero solution and the solutions that never vanish. That every solution of $P' = kP$ on an interval is $P_0\,e^{kt}$ is the uniqueness half of [[§21 Exponential Growth and Decay#^thm-21-1|Theorem §21.1]] with $y = P$ (see [[§21 Exponential Growth and Decay#^pf-21-1|its proof]]).

^pf-60-1

*Uses:* [[§59 Separable Equations#^thm-59-1|§59.1]], [[§21 Exponential Growth and Decay#^thm-21-1|§21.1]] (every solution of $y' = ky$)

> [!remark]- Connections
> - The uniqueness half, proved in [[§21 Exponential Growth and Decay#^pf-21-1|the proof of Theorem §21.1]], rests on [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (a vanishing derivative means constant), proved there from the Mean Value Theorem.

> [!remark] Remark: Emigration
> Emigration (or "harvesting") at a constant rate $m$ changes Equation 1 into
>
> $$
> \frac{dP}{dt} = kP - m . \qquad (3)
> $$
>
> Stewart leaves its solution to the exercises (Exercise 17). It is again separable, and for $k \ne 0$ the same steps give $P(t) = \dfrac{m}{k} + \Big(P_0 - \dfrac{m}{k}\Big)e^{kt}$. With $k > 0$ the population grows exponentially if $m < kP_0$, stays constant if $m = kP_0$, and declines if $m > kP_0$.

^rem-60-1

## The Logistic Model

As discussed in [[§57 Modeling with Differential Equations|§57]], a population often increases exponentially in its early stages but levels off eventually, because of limited resources. So we want $dP/dt \approx kP$ when $P$ is small: the relative growth rate is almost constant for a small population. But the relative growth rate should also decrease as $P$ increases, and become negative if $P$ ever exceeds the largest population the environment can sustain. The simplest expression for the relative growth rate with these properties is

$$
\frac{dP/dt}{P} = k\Big(1 - \frac{P}{M}\Big) .
$$

> [!definition] Definition §60.2: Carrying Capacity and the Logistic Equation
> The **carrying capacity** $M$ of an environment is the maximum population that the environment is capable of sustaining in the long run. Multiplying the relative growth rate $k(1 - P/M)$ by $P$ gives the **logistic differential equation**
>
> $$
> \frac{dP}{dt} = kP\Big(1 - \frac{P}{M}\Big) . \qquad (4)
> $$
>
> Here $k > 0$ and $M > 0$ are constants.
>
> *Stewart: 9.4, Equation 4*

^def-60-2

> [!remark] Remark: Reading the Logistic Equation
> Information about the solutions can be read off Equation 4 before solving it.
> - If $P$ is small compared with $M$, then $P/M \approx 0$ and $dP/dt \approx kP$: natural growth.
> - If $P \to M$, then $P/M \to 1$ and $dP/dt \to 0$.
> - If $0 < P < M$, the right side is positive, so $dP/dt > 0$ and the population increases.
> - If $P > M$, then $1 - P/M < 0$, so $dP/dt < 0$ and the population decreases.
> - The constant functions $P = 0$ and $P = M$ are **equilibrium solutions** ([[§57 Modeling with Differential Equations#^def-57-3|Definition §57.3]]).

^rem-60-2

> [!example] Example §60.1: The Direction Field of a Logistic Equation
> Draw a direction field for the logistic equation with $k = 0.08$ and carrying capacity $M = 1000$. What can you deduce about the solutions?
>
> The equation is
>
> $$
> \frac{dP}{dt} = 0.08P\Big(1 - \frac{P}{1000}\Big) .
> $$
>
> Only the first quadrant matters, since negative populations are not meaningful and we are interested in $t \ge 0$. The equation is **autonomous** ($dP/dt$ depends only on $P$, not on $t$; [[§58 Direction Fields and Euler's Method#^def-58-3|Definition §58.3]]), so the slopes are the same along any horizontal line. The slopes are positive for $0 < P < 1000$ and negative for $P > 1000$. They are small when $P$ is close to $0$ or to $1000$. The solutions move away from the equilibrium solution $P = 0$ and toward the equilibrium solution $P = 1000$.
>
> Sketching solution curves with initial populations $P(0) = 100$, $400$ and $1300$ in the field: curves that start below $P = 1000$ increase, and the one that starts above decreases. The slope $0.08P(1 - P/1000)$ is largest at $P = 500$ (a downward parabola in $P$, with zeros $0$ and $1000$). So the curves that start below $500$ get steeper until $P \approx 500$ and less steep afterward: they have inflection points near $P = 500$. Proposition §60.3 shows that the inflection happens exactly at $P = 500$.
>
> *Stewart: Example 9.4.1*

^ex-60-1

![[m233-60-1.svg]]
*The direction field of $dP/dt = 0.08P(1 - P/1000)$ (gray) and the solutions with $P(0) = 100, 400, 1300$ (blue), drawn from the formula of Theorem §60.2. The slopes depend only on $P$. All three curves approach the equilibrium $P = M = 1000$ (green). The two curves that start below $M/2 = 500$ have their inflection points (red) exactly on the line $P = 500$, at $t = \frac{\ln 9}{0.08} \approx 27.5$ and $t = \frac{\ln 1.5}{0.08} \approx 5.1$.*

The logistic equation is separable, so it can be solved explicitly with the method of [[§59 Separable Equations|§59]].

> [!theorem] Theorem §60.2: Solution of the Logistic Equation
> The solution of the logistic equation (4) with initial population $P(0) = P_0 > 0$ is
>
> $$
> P(t) = \frac{M}{1 + A\,e^{-kt}}, \qquad\text{where}\quad A = \frac{M - P_0}{P_0} . \qquad (7)
> $$
>
> In particular,
>
> $$
> \lim_{t \to \infty} P(t) = M ,
> $$
>
> as expected.
>
> *Stewart: 9.4, Equation 7*

^thm-60-2

> [!proof]+ Proof
> If $P_0 = M$, then $A = 0$ and (7) is the equilibrium solution $P = M$. Otherwise $P \ne 0, M$, and separating variables in (4) gives
>
> $$
> \int \frac{dP}{P(1 - P/M)} = \int k\,dt . \qquad (5)
> $$
>
> To evaluate the left side, write $\dfrac{1}{P(1 - P/M)} = \dfrac{M}{P(M - P)}$ and use partial fractions ([[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|Theorem §47.3]]):
>
> $$
> \frac{M}{P(M - P)} = \frac{1}{P} + \frac{1}{M - P}
> $$
>
> (indeed $\frac1P + \frac{1}{M - P} = \frac{(M - P) + P}{P(M - P)}$). So Equation 5 becomes
>
> $$
> \int \Big(\frac{1}{P} + \frac{1}{M - P}\Big)\,dP = \int k\,dt
> \qquad\Longrightarrow\qquad
> \ln|P| - \ln|M - P| = kt + C .
> $$
>
> Hence
>
> $$
> \ln\left|\frac{M - P}{P}\right| = -kt - C, \qquad
> \left|\frac{M - P}{P}\right| = e^{-kt - C} = e^{-C} e^{-kt}, \qquad
> \frac{M - P}{P} = A\,e^{-kt} , \qquad (6)
> $$
>
> where $A = \pm e^{-C}$. (The sign is constant, because $(M - P)/P$ is continuous and never $0$ on an interval where $P \ne 0, M$.) Solving (6) for $P$:
>
> $$
> \frac{M}{P} - 1 = A\,e^{-kt} \quad\Longrightarrow\quad \frac{P}{M} = \frac{1}{1 + A\,e^{-kt}} \quad\Longrightarrow\quad P = \frac{M}{1 + A\,e^{-kt}} .
> $$
>
> To find $A$, put $t = 0$ in (6), where $P = P_0$: $\dfrac{M - P_0}{P_0} = A\,e^{0} = A$.
>
> **The formula is valid for all $t \ge 0$.** Since $P_0 > 0$, $A = M/P_0 - 1 > -1$. If $A \ge 0$, then $1 + A\,e^{-kt} \ge 1$. If $-1 < A < 0$ (that is, $P_0 > M$), then for $t \ge 0$ we have $0 < e^{-kt} \le 1$, so $1 + A\,e^{-kt} \ge 1 + A > 0$. Either way the denominator is positive. (Stewart does not discuss this.)
>
> **The limit.** Since $k > 0$, $e^{-kt} \to 0$ as $t \to \infty$ ([[§11 Limits at Infinity; Horizontal Asymptotes#^thm-11-4|Theorem §11.4]]), so $P(t) \to M/(1 + 0) = M$.

^pf-60-2

*Uses:* [[§59 Separable Equations#^thm-59-1|§59.1]], [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-3|§47.3]] (partial fractions), [[§11 Limits at Infinity; Horizontal Asymptotes#^thm-11-4|§11.4]] (limit of an exponential at infinity)

> [!theorem] Proposition §60.3: Inflection at Half the Carrying Capacity
> If $P$ satisfies the logistic equation (4), then
>
> $$
> \frac{d^2P}{dt^2} = k^2 P\Big(1 - \frac{P}{M}\Big)\Big(1 - \frac{2P}{M}\Big) .
> $$
>
> Consequently a solution with $0 < P(0) < M/2$ has an inflection point exactly when $P = M/2$, and the population grows fastest at that moment.
>
> *Stewart: 9.4 (text); Exercise 13*

^prop-60-3

> [!proof]+ Proof
> Write (4) as $P' = kP - \frac{k}{M}P^2$ and differentiate with respect to $t$, using the Chain Rule ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]):
>
> $$
> P'' = \Big(k - \frac{2k}{M}P\Big)P' = k\Big(1 - \frac{2P}{M}\Big) \cdot kP\Big(1 - \frac{P}{M}\Big) = k^2 P\Big(1 - \frac{P}{M}\Big)\Big(1 - \frac{2P}{M}\Big) .
> $$
>
> Now let $0 < P_0 < M/2$, so $A = (M - P_0)/P_0 > 1$ in Theorem §60.2. Then $0 < P(t) < M$ for all $t \ge 0$, so $P$ is increasing ([[§60 Models for Population Growth#^rem-60-2|Remark: Reading the Logistic Equation]]). By (7), $P(t) = M/2$ exactly when $A\,e^{-kt} = 1$, that is, at $t^* = (\ln A)/k > 0$. For $0 \le t < t^*$ we have $P < M/2$, so all three factors $P$, $1 - P/M$, $1 - 2P/M$ are positive and $P'' > 0$. For $t > t^*$ we have $M/2 < P < M$, so $1 - 2P/M < 0$ and $P'' < 0$. So the graph changes from concave upward to concave downward at $t^*$: an inflection point ([[§27 What Derivatives Tell Us About the Shape of a Graph#^def-27-2|Definition §27.2]]). There $P'$ changes from increasing to decreasing, so $P'$ has its maximum at $t^*$: the population grows fastest when it reaches half its carrying capacity.

^pf-60-3

*Uses:* [[§60 Models for Population Growth#^thm-60-2|§60.2]], [[§17 The Chain Rule#^thm-17-2|§17.2]] (Chain Rule), [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|§27.1]] (Increasing/Decreasing Test, applied to $P'$), [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-3|§27.3]] (Concavity Test), [[§27 What Derivatives Tell Us About the Shape of a Graph#^def-27-2|Def. §27.2]] (inflection point)

The same formula shows that a solution starting at $M/2 \le P_0 < M$ is concave downward for all $t > 0$, and one starting above $M$ is concave upward (then $1 - P/M$ and $1 - 2P/M$ are both negative).

> [!example] Example §60.2: Using the Logistic Formula
> Write the solution of the initial-value problem
>
> $$
> \frac{dP}{dt} = 0.08P\Big(1 - \frac{P}{1000}\Big), \qquad P(0) = 100 ,
> $$
>
> and use it to find the population sizes $P(40)$ and $P(80)$. At what time does the population reach $900$?
>
> This is a logistic equation with $k = 0.08$, carrying capacity $M = 1000$ and initial population $P_0 = 100$. By Theorem §60.2,
>
> $$
> P(t) = \frac{1000}{1 + A\,e^{-0.08t}}, \qquad A = \frac{1000 - 100}{100} = 9, \qquad\text{so}\qquad P(t) = \frac{1000}{1 + 9e^{-0.08t}} .
> $$
>
> The population sizes at $t = 40$ and $t = 80$ are
>
> $$
> P(40) = \frac{1000}{1 + 9e^{-3.2}} \approx 731.6, \qquad P(80) = \frac{1000}{1 + 9e^{-6.4}} \approx 985.3 .
> $$
>
> The population reaches $900$ when
>
> $$
> \frac{1000}{1 + 9e^{-0.08t}} = 900
> \quad\Longrightarrow\quad 1 + 9e^{-0.08t} = \frac{10}{9}
> \quad\Longrightarrow\quad e^{-0.08t} = \frac{1}{81}
> \quad\Longrightarrow\quad -0.08t = \ln\frac{1}{81} = -\ln 81 ,
> $$
>
> so
>
> $$
> t = \frac{\ln 81}{0.08} \approx 54.9 .
> $$
>
> So the population reaches $900$ when $t$ is approximately $55$. This is the lowest curve in the figure above; its inflection point, where $P = 500$, is at $t = (\ln 9)/0.08 \approx 27.5$ by Proposition §60.3.
>
> *Stewart: Example 9.4.2*

^ex-60-2

## Comparison of the Natural Growth and Logistic Models

In the 1930s the biologist G. F. Gause conducted an experiment with the protozoan *Paramecium* and used a logistic equation to model his data. He counted the population daily, estimated the initial relative growth rate to be $0.7944$ and the carrying capacity to be $64$.

> [!example] Example §60.3: Gause's Paramecium Data
> Find the exponential and logistic models for Gause's data (the row "observed" in the table below). Compare the predicted values with the observed values and comment on the fit for each model.
>
> **Exponential model.** With relative growth rate $k = 0.7944$ and initial population $P_0 = 2$, Theorem §60.1 gives
>
> $$
> P(t) = P_0\,e^{kt} = 2e^{0.7944t} .
> $$
>
> **Logistic model.** Gause used the same value of $k$. This is reasonable because $P_0 = 2$ is small compared with $M = 64$: the initial relative growth rate of the logistic model is
>
> $$
> \frac{1}{P_0}\,\frac{dP}{dt}\bigg|_{t = 0} = k\Big(1 - \frac{2}{64}\Big) \approx k ,
> $$
>
> very close to the value for the exponential model. Theorem §60.2 gives
>
> $$
> P(t) = \frac{64}{1 + A\,e^{-0.7944t}}, \qquad A = \frac{M - P_0}{P_0} = \frac{64 - 2}{2} = 31, \qquad\text{so}\qquad P(t) = \frac{64}{1 + 31e^{-0.7944t}} .
> $$
>
> **Comparison.** The predicted values, rounded to the nearest integer:
>
> | $t$ (days) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> | $P$ (observed) | 2 | 3 | 22 | 16 | 39 | 52 | 54 | 47 | 50 | 76 | 69 | 51 | 57 | 70 | 53 | 59 | 57 |
> | $P$ (logistic) | 2 | 4 | 9 | 17 | 28 | 40 | 51 | 57 | 61 | 62 | 63 | 64 | 64 | 64 | 64 | 64 | 64 |
> | $P$ (exponential) | 2 | 4 | 10 | 22 | 48 | 106 | 235 | … | | | | | | | | | |
>
> For the first three or four days the exponential model gives results comparable to those of the logistic model. For $t \ge 5$ the exponential model is hopelessly inaccurate (it predicts $106$ against an observed $52$, and the error keeps growing), but the logistic model fits the observations reasonably well.
>
> *Stewart: Example 9.4.3*

^ex-60-3

![[m233-60-2.svg]]
*Gause's daily counts (blue dots) with the exponential model $2e^{0.7944t}$ (green) and the logistic model $64/(1 + 31e^{-0.7944t})$ (red). The two models start out together, since $P_0 = 2$ is small compared with $M = 64$. The exponential curve leaves the data after about four days, while the logistic curve levels off at the carrying capacity, around which the counts scatter.*

Many countries that formerly experienced exponential growth now find their rates of population growth declining, and the logistic model fits better. Stewart's example is the population of Japan, 1960–2015 (in thousands, with $t = 0$ in 1960). A logistic function shifted upward, fitted by regression on a calculator, is $P = 90{,}000 + \dfrac{37{,}419}{1 + 6.56e^{-0.14t}}$, and it follows the data closely.

## Other Models for Population Growth

> [!definition] Definition §60.3: Logistic Models with Harvesting and with a Minimum Population
> Two modifications of the logistic equation (4), with constants $k, M > 0$:
> - **Harvesting.** For a population harvested at a constant rate $c > 0$ (think of a population of fish caught at a constant rate),
>
>   $$
>   \frac{dP}{dt} = kP\Big(1 - \frac{P}{M}\Big) - c .
>   $$
>
> - **Minimum population.** For a species that tends to become extinct below a minimum population level $m$ (adults may not be able to find suitable mates),
>
>   $$
>   \frac{dP}{dt} = kP\Big(1 - \frac{P}{M}\Big)\Big(1 - \frac{m}{P}\Big) ,
>   $$
>
>   where the extra factor $1 - m/P$ takes into account the consequences of a sparse population: it is negative for $0 < P < m$, so a population below $m$ decreases.
>
> *Stewart: 9.4 (text)*

^def-60-3

Stewart treats these two equations in Exercises 19–21, and two further models in the exercises: the Gompertz growth function (Exercise 22) and seasonal-growth models (Exercises 23 and 24).
