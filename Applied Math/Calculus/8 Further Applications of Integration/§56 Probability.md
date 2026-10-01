---
type: section
subject: "[[Calculus]]"
chapter: 8
section: 56
stewart: "8.5"
aliases: ["Stewart 8.5"]
tags: [calculus]
---
← [[§55 Applications to Economics and Biology]] · ↑ [[· 8 Further Applications of Integration]] · [[§57 Modeling with Differential Equations]] →

*Stewart, Section 8.5.*

A continuous random variable (a height, a lifetime, a waiting time) is described by a probability density function $f$: the probability that the variable lies in an interval is the area under the graph of $f$ over that interval. So probabilities are definite integrals, and the requirement that the total probability is $1$ is an improper integral ([[§51 Improper Integrals|§51]]). This section sets up densities, computes the mean (which turns out to be the $x$-coordinate of a centroid, as in [[§54 Applications to Physics and Engineering|§54]]) and the median, and introduces the two most used families: the exponential densities, which model waiting times, and the normal densities, whose integrals have no elementary antiderivative and must be computed numerically.

## Probability Density Functions

> [!definition] Definition §56.1: Continuous Random Variable
> A **continuous random variable** is a quantity whose values range over an interval of real numbers, such as the cholesterol level, the height or the battery lifetime of an individual chosen at random (even if it is only measured or recorded to the nearest integer). For a random variable $X$, the probability that $X$ lies between $a$ and $b$ is written
>
> $$
> P(a \le X \le b) .
> $$
>
> In the frequency interpretation, this is the long-run proportion of individuals whose value lies between $a$ and $b$. Being a proportion, it lies between $0$ and $1$.
>
> *Stewart: 8.5 (text)*

^def-56-1

> [!definition] Definition §56.2: Probability Density Function
> Every continuous random variable $X$ has a **probability density function** $f$. This means that the probability that $X$ lies between $a$ and $b$ is the integral of $f$ from $a$ to $b$:
>
> $$
> P(a \le X \le b) = \int_a^b f(x)\,dx .
> $$
>
> Geometrically, $P(a \le X \le b)$ is the area under the graph of $f$ from $a$ to $b$.
>
> *Stewart: 8.5, Equation 1*

^def-56-2

> [!theorem] Proposition §56.1: The Two Properties of a Density
> The probability density function $f$ of a random variable $X$ satisfies
>
> $$
> f(x) \ge 0 \quad \text{for all } x \qquad\text{and}\qquad \int_{-\infty}^{\infty} f(x)\,dx = 1 .
> $$
>
> Conversely, a function with these two properties is the density of a random variable; checking them is how one verifies that a given $f$ "is a probability density function" (Example §56.1).
>
> *Stewart: 8.5, Equation 2*

^prop-56-1

> [!remark] Remark: Why It Works
> Stewart argues from the meaning of probability, not from a formal definition. If $f$ were negative on some interval $[a, b]$, then $P(a \le X \le b) = \int_a^b f(x)\,dx$ would be negative, which a proportion cannot be. And $X$ certainly takes *some* real value, so the probability that it lies in $(-\infty, \infty)$ is $1$. In the language of [[§51 Improper Integrals|§51]], $\int_a^b f(x)\,dx \to 1$ as $a \to -\infty$ and $b \to \infty$.

^rem-56-1

> [!remark]- Connections
> - The rigorous setting: a **distribution function** $F(t) = P(X \le t)$ is increasing with $F(-\infty) = 0$, $F(\infty) = 1$, and a density is a $g \ge 0$ with $F(t) = \int_{-\infty}^t g(x)\,dx$, so that $F' = g$ where $g$ is continuous: [[§36 Improper Integrals#^rem-36-3|451 Remark: Distribution functions]]. The improper integrals involved: [[§36 Improper Integrals#^def-36-1|451 Def. §36.1]], [[§36 Improper Integrals#^def-36-2|451 Def. §36.2]].

> [!remark] Remark: Single Values Have Probability Zero
> Densities are always used with *intervals* of values. A density function says nothing useful about the probability that $X$ *equals* $a$: by Definition §56.2 that probability is $\int_a^a f(x)\,dx = 0$. In particular $P(a \le X \le b) = P(a < X < b)$, so it does not matter whether the endpoints are included. The value $f(a)$ itself is not a probability (it can exceed $1$); only areas under $f$ are.

^rem-56-2

> [!example] Example §56.1: Checking a Density
> Let $f(x) = 0.006x(10 - x)$ for $0 \le x \le 10$ and $f(x) = 0$ for all other values of $x$.
> (a) Verify that $f$ is a probability density function. (b) Find $P(4 \le X \le 8)$.
>
> **(a)** For $0 \le x \le 10$ both $x \ge 0$ and $10 - x \ge 0$, so $0.006x(10 - x) \ge 0$; elsewhere $f(x) = 0$. Hence $f(x) \ge 0$ for all $x$. Since $f = 0$ outside $[0, 10]$, the improper integral reduces to an ordinary one:
>
> $$
> \int_{-\infty}^{\infty} f(x)\,dx = \int_0^{10} 0.006x(10 - x)\,dx = 0.006 \int_0^{10} (10x - x^2)\,dx = 0.006 \Big[5x^2 - \tfrac13 x^3\Big]_0^{10} = 0.006\Big(500 - \frac{1000}{3}\Big) = 0.006 \cdot \frac{500}{3} = 1 .
> $$
>
> By Proposition §56.1, $f$ is a probability density function.
>
> **(b)**
>
> $$
> P(4 \le X \le 8) = \int_4^8 f(x)\,dx = 0.006 \Big[5x^2 - \tfrac13 x^3\Big]_4^8 = 0.006\Big[\Big(320 - \frac{512}{3}\Big) - \Big(80 - \frac{64}{3}\Big)\Big] = 0.006\Big(240 - \frac{448}{3}\Big) = 0.006 \cdot \frac{272}{3} = 0.544 .
> $$
>
> *Stewart: Example 8.5.1*

^ex-56-1

![[m233-56-1.svg]]
*The density of Example §56.1. The whole area under the graph is $1$ (all outcomes together), and the probability $P(4 \le X \le 8) = 0.544$ is the shaded part of it. The graph is $0$ outside $[0, 10]$: the variable never takes values there.*

> [!example] Example §56.2: The Form of an Exponential Density
> Waiting times and equipment failure times are commonly modeled by exponentially decreasing probability density functions. Find the exact form of such a function.
>
> Let $t$ (in minutes) be the time you wait on hold before an agent answers your call, placed at time $t = 0$, and $f$ its density. By Definition §56.2, $\int_0^2 f(t)\,dt$ is the probability that an agent answers within the first two minutes, and $\int_4^5 f(t)\,dt$ the probability that the call is answered during the fifth minute.
>
> The agent cannot answer before the call is placed, so $f(t) = 0$ for $t < 0$. For $t \ge 0$ we are told that $f$ decreases exponentially, $f(t) = Ae^{-ct}$ with constants $A, c > 0$. So
>
> $$
> f(t) = \begin{cases} 0 & \text{if } t < 0 \\ Ae^{-ct} & \text{if } t \ge 0 \end{cases}
> $$
>
> and $f \ge 0$. The second condition of Proposition §56.1 determines $A$:
>
> $$
> \begin{aligned}
> 1 &= \int_{-\infty}^{\infty} f(t)\,dt = \int_{-\infty}^{0} f(t)\,dt + \int_0^{\infty} f(t)\,dt = 0 + \int_0^{\infty} Ae^{-ct}\,dt = \lim_{x \to \infty} \int_0^x Ae^{-ct}\,dt \\
> &= \lim_{x \to \infty} \Big[-\frac{A}{c}e^{-ct}\Big]_0^x = \lim_{x \to \infty} \frac{A}{c}\big(1 - e^{-cx}\big) = \frac{A}{c} ,
> \end{aligned}
> $$
>
> since $e^{-cx} \to 0$ for $c > 0$. Therefore $A/c = 1$, that is, $A = c$.
>
> *Stewart: Example 8.5.2*

^ex-56-2

> [!definition] Definition §56.3: Exponential Density Function
> For a constant $c > 0$, the **exponential density function** is
>
> $$
> f(t) = \begin{cases} 0 & \text{if } t < 0 \\ ce^{-ct} & \text{if } t \ge 0 . \end{cases}
> $$
>
> By Example §56.2, every exponentially decreasing density on $[0, \infty)$ has this form. Its graph starts at height $c$ at $t = 0$ and decays to $0$.
>
> *Stewart: 8.5 (Example 2)*

^def-56-3

## Average Values

> [!remark] Remark: Where the Mean Comes From
> Let $f$ be the density of the waiting time $t$ for a phone call, and suppose nobody waits more than an hour, so we work on $0 \le t \le 60$. Divide $[0, 60]$ into $n$ intervals $[t_{i-1}, t_i]$ of length $\Delta t$ with midpoints $\bar t_i$. The probability that a call is answered between $t_{i-1}$ and $t_i$ is the area under $y = f(t)$ there, approximately $f(\bar t_i)\,\Delta t$ (one midpoint rectangle). So out of $N$ callers about $N f(\bar t_i)\,\Delta t$ are answered in that period, and each of them waited about $\bar t_i$. The total waiting time of all callers is about
>
> $$
> \sum_{i=1}^n \bar t_i \big[N f(\bar t_i)\,\Delta t\big] ,
> \qquad\text{so the average is about}\qquad
> \sum_{i=1}^n \bar t_i\, f(\bar t_i)\,\Delta t .
> $$
>
> This is a Riemann sum for $t f(t)$ ([[§35 The Definite Integral|§35]]). As $\Delta t \to 0$ and $n \to \infty$ it tends to $\int_0^{60} t f(t)\,dt$, the **mean waiting time**.

^rem-56-3

> [!definition] Definition §56.4: Mean
> The **mean** of a probability density function $f$ is
>
> $$
> \mu = \int_{-\infty}^{\infty} x f(x)\,dx .
> $$
>
> It is the long-run average value of the random variable $X$, and also a measure of the centrality of $f$. (The Greek letter $\mu$, "mu", is traditional.)
>
> *Stewart: 8.5 (text)*

^def-56-4

> [!theorem] Proposition §56.2: The Mean Is the Balance Point
> Let $\mathscr{R}$ be the region under the graph of a density $f$. The $x$-coordinate of the centroid of $\mathscr{R}$ is the mean $\mu$. So a thin plate in the shape of $\mathscr{R}$ balances at a point on the vertical line $x = \mu$.
>
> *Stewart: 8.5 (text)*

^prop-56-2

> [!proof]+ Proof
> By the centroid formula for a region under a graph (Formula 8.3.8, [[§54 Applications to Physics and Engineering|§54]]), here over the whole line,
>
> $$
> \bar x = \frac{\displaystyle\int_{-\infty}^{\infty} x f(x)\,dx}{\displaystyle\int_{-\infty}^{\infty} f(x)\,dx} = \int_{-\infty}^{\infty} x f(x)\,dx = \mu ,
> $$
>
> because the denominator, the area of $\mathscr{R}$, equals $1$ by Proposition §56.1.

^pf-56-2

*Uses:* [[§56 Probability#^prop-56-1|§56.1]], [[§56 Probability#^def-56-4|Def. §56.4]], [[§54 Applications to Physics and Engineering|§54]] (centroid of a plane region, Formula 8.3.8)

> [!example] Example §56.3: The Mean of an Exponential Density
> Find the mean of the exponential distribution of Example §56.2, $f(t) = 0$ for $t < 0$ and $f(t) = ce^{-ct}$ for $t \ge 0$.
>
> By Definition §56.4,
>
> $$
> \mu = \int_{-\infty}^{\infty} t f(t)\,dt = \int_0^{\infty} tce^{-ct}\,dt .
> $$
>
> Integrate by parts ([[§44 Integration by Parts|§44]]) with $u = t$, $dv = ce^{-ct}\,dt$, so $du = dt$ and $v = -e^{-ct}$:
>
> $$
> \int_0^{\infty} tce^{-ct}\,dt = \lim_{x \to \infty} \int_0^x tce^{-ct}\,dt = \lim_{x \to \infty} \Big( \Big[-te^{-ct}\Big]_0^x + \int_0^x e^{-ct}\,dt \Big) = \lim_{x \to \infty} \Big( -xe^{-cx} + \frac1c - \frac{e^{-cx}}{c} \Big) = \frac1c .
> $$
>
> The first term tends to $0$ by l'Hospital's Rule ([[§28 Indeterminate Forms and L'Hospital's Rule|§28]]): $\displaystyle\lim_{x \to \infty} \frac{x}{e^{cx}} = \lim_{x \to \infty} \frac{1}{ce^{cx}} = 0$. The last term tends to $0$ since $c > 0$.
>
> So $\mu = 1/c$, and the exponential density can be written in terms of its mean as
>
> $$
> f(t) = \begin{cases} 0 & \text{if } t < 0 \\ \mu^{-1} e^{-t/\mu} & \text{if } t \ge 0 . \end{cases}
> $$
>
> *Stewart: Example 8.5.3*

^ex-56-3

> [!example] Example §56.4: Waiting on Hold
> Suppose the average waiting time for a customer's call to be answered by a customer service agent is five minutes, and that an exponential distribution is appropriate.
> (a) Find the probability that a call is answered during the first minute.
> (b) Find the probability that a customer waits on hold for more than five minutes.
> (c) Find the median waiting time (Definition §56.5 below).
>
> The mean is $\mu = 5$ min, so by Example §56.3 the density is $f(t) = 0$ for $t < 0$ and $f(t) = \frac15 e^{-t/5} = 0.2e^{-t/5}$ for $t \ge 0$ ($t$ in minutes).
>
> **(a)**
>
> $$
> P(0 \le T \le 1) = \int_0^1 0.2e^{-t/5}\,dt = 0.2(-5)e^{-t/5}\Big]_0^1 = 1 - e^{-1/5} \approx 0.1813 .
> $$
>
> So about $18\%$ of customers' calls are answered during the first minute.
>
> **(b)**
>
> $$
> P(T > 5) = \int_5^{\infty} 0.2e^{-t/5}\,dt = \lim_{x \to \infty} \int_5^x 0.2e^{-t/5}\,dt = \lim_{x \to \infty} \big(e^{-1} - e^{-x/5}\big) = \frac1e - 0 \approx 0.368 .
> $$
>
> About $37\%$ of customers wait on hold more than five minutes.
>
> **(c)** The median $m$ satisfies $\int_m^{\infty} 0.2e^{-t/5}\,dt = \frac12$. As in (b), the left side is $e^{-m/5}$, so $e^{-m/5} = \frac12$, that is, $m = 5\ln 2 \approx 3.47$ minutes. Half of the callers are answered within about $3.5$ minutes.
>
> *Stewart: Example 8.5.4 and Exercise 8.5.9*

^ex-56-4

![[m233-56-2.svg]]
*The waiting-time density of Example §56.4. The blue area over $[0, 1]$ is the $18\%$ answered in the first minute; the red tail beyond $t = 5$ is the $37\%$ who wait longer than the mean. The median (green) splits the total area into two halves and lies to the left of the mean: the long right tail of rare long waits pulls the mean (the balance point, Proposition §56.2) to the right.*

> [!remark] Remark: Mean Versus Typical Value
> In Example §56.4(b), the mean waiting time is $5$ minutes, yet only $37\%$ of callers wait more than $5$ minutes. The reason is that some callers have to wait much longer (maybe $10$ or $15$ minutes), and this brings up the average. A measure of centrality that is not pulled by such long waits is the median.

^rem-56-4

> [!definition] Definition §56.5: Median
> The **median** of a probability density function $f$ is the number $m$ such that
>
> $$
> \int_m^{\infty} f(x)\,dx = \frac12 .
> $$
>
> Half of the area under the graph of $f$ lies to the right of $m$ (and so, by Proposition §56.1, half lies to the left). For waiting times: half of the callers wait less than $m$ and half wait longer.
>
> *Stewart: 8.5 (text)*

^def-56-5

## Normal Distributions

> [!definition] Definition §56.6: Normal Distribution
> A random variable $X$ has a **normal distribution** if its probability density function is a member of the family
>
> $$
> f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(x - \mu)^2/(2\sigma^2)} ,
> $$
>
> where $\mu$ is a constant and $\sigma > 0$. The positive constant $\sigma$ (lowercase Greek "sigma") is the **standard deviation**: it measures how spread out the values of $X$ are. Normal distributions model test scores on aptitude tests, heights and weights of individuals from a homogeneous population, annual rainfall at a given location, and many other random phenomena.
>
> *Stewart: 8.5, Equation 3*

^def-56-6

> [!theorem] Proposition §56.3: The Normal Density Is a Density with Mean μ
> For every $\mu$ and every $\sigma > 0$, the function $f$ of Definition §56.6 is a probability density function,
>
> $$
> \int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(x - \mu)^2/(2\sigma^2)}\,dx = 1 ,
> $$
>
> and its mean is $\mu$.
>
> *Stewart: 8.5 (text; the integral is Exercise 15.3.48)*

^prop-56-3

> [!proof]+ Proof
> Stewart leaves both facts to the reader ("you can verify"; the integral "can be verified using the methods of multivariable calculus"). Here is the computation. Clearly $f > 0$.
>
> **Total area.** Substitute $x = \mu + \sigma\sqrt2\,u$, $dx = \sigma\sqrt2\,du$ ([[§38 The Substitution Rule|§38]]; on each finite interval, then pass to the limit). Then $(x - \mu)^2/(2\sigma^2) = u^2$ and
>
> $$
> \int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(x - \mu)^2/(2\sigma^2)}\,dx = \frac{\sigma\sqrt2}{\sigma\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-u^2}\,du = \frac{1}{\sqrt\pi} \cdot \sqrt\pi = 1 .
> $$
>
> The value $\int_{-\infty}^{\infty} e^{-u^2}\,du = \sqrt\pi$ is computed in Section 15.3 by squaring the integral and passing to polar coordinates ([[§100 Double Integrals in Polar Coordinates|§100]]).
>
> **Mean.** Write $x = \mu + (x - \mu)$ and use the total area:
>
> $$
> \int_{-\infty}^{\infty} x f(x)\,dx = \mu \int_{-\infty}^{\infty} f(x)\,dx + \frac{1}{\sigma\sqrt{2\pi}} \int_{-\infty}^{\infty} (x - \mu)\, e^{-(x - \mu)^2/(2\sigma^2)}\,dx = \mu \cdot 1 + 0 = \mu .
> $$
>
> The second integral is $0$: an antiderivative of $(x - \mu)e^{-(x - \mu)^2/(2\sigma^2)}$ is $-\sigma^2 e^{-(x - \mu)^2/(2\sigma^2)}$, which tends to $0$ as $x \to \pm\infty$, so both halves $\int_{-\infty}^{\mu}$ and $\int_{\mu}^{\infty}$ converge, to $-\sigma^2$ and $\sigma^2$, and they cancel.

^pf-56-3

*Uses:* [[§56 Probability#^def-56-4|Def. §56.4]], [[§38 The Substitution Rule|§38]], [[§51 Improper Integrals|§51]], [[§100 Double Integrals in Polar Coordinates|§100]] (the integral of e to the minus u squared)

> [!remark]- Connections
> - The normal density and its distribution function, with the value √π taken on credit: [[§36 Improper Integrals#^ex-36-4|451 Ex. §36.4]]; the value √π itself, by polar coordinates: [[§15 Multivariable Integration#^ex-15-7|452 Ex. §15.7]].

> [!remark] Remark: The Shape of the Normal Densities
> The graph of $f$ is a bell-shaped curve, symmetric about the line $x = \mu$, with its peak $\frac{1}{\sigma\sqrt{2\pi}}$ at $x = \mu$. For small $\sigma$ the values of $X$ are clustered about the mean (a tall narrow bell); for larger $\sigma$ they are more spread out (a low wide bell). The factor $1/(\sigma\sqrt{2\pi})$ is exactly what makes the total area $1$ (Proposition §56.3). Statisticians have methods for estimating $\mu$ and $\sigma$ from data.

^rem-56-5

> [!example] Example §56.5: IQ Scores
> Intelligence Quotient (IQ) scores are distributed normally with mean $100$ and standard deviation $15$.
> (a) What percentage of the population has an IQ score between $85$ and $115$?
> (b) What percentage of the population has an IQ above $140$?
>
> Use Definition §56.6 with $\mu = 100$, $\sigma = 15$, so $2\sigma^2 = 450$.
>
> **(a)**
>
> $$
> P(85 \le X \le 115) = \int_{85}^{115} \frac{1}{15\sqrt{2\pi}}\, e^{-(x - 100)^2/450}\,dx .
> $$
>
> The function $e^{-x^2}$ has no elementary antiderivative ([[§48 Strategy for Integration|§48]]), so this integral cannot be evaluated exactly. Numerical integration (a calculator, or the Midpoint Rule or Simpson's Rule of [[§50 Approximate Integration|§50]]) gives
>
> $$
> P(85 \le X \le 115) \approx 0.68 .
> $$
>
> So about $68\%$ of the population has an IQ between $85$ and $115$, that is, within one standard deviation of the mean.
>
> **(b)**
>
> $$
> P(X > 140) = \int_{140}^{\infty} \frac{1}{15\sqrt{2\pi}}\, e^{-(x - 100)^2/450}\,dx .
> $$
>
> To avoid the improper integral, approximate it by the integral from $140$ to $200$ (people with an IQ over $200$ are extremely rare: the neglected tail is about $10^{-11}$). Numerically,
>
> $$
> P(X > 140) \approx \int_{140}^{200} \frac{1}{15\sqrt{2\pi}}\, e^{-(x - 100)^2/450}\,dx \approx 0.0038 .
> $$
>
> So about $0.4\%$ of the population has an IQ over $140$.
>
> *Stewart: Example 8.5.5*

^ex-56-5

Probabilities for two random variables at once (joint density functions) are double integrals; they come in Section 15.4 ([[§101 Applications of Double Integrals|§101]]).
