---
type: section
subject: "[[Calculus]]"
chapter: 9
section: 62
stewart: "9.6"
aliases: ["Stewart 9.6"]
tags: [calculus]
---
← [[§61 Linear Equations]] · ↑ [[· 9 Differential Equations]] · [[§63 Curves Defined by Parametric Equations]] →

*Stewart, Section 9.6.*

The population models so far describe one species living alone. This section couples two: a prey species with an ample food supply and a predator species that feeds on it. The result is a pair of linked differential equations, the Lotka–Volterra equations. They can rarely be solved by explicit formulas, so they are analysed graphically. Dividing one equation by the other gives a single first-order equation for the curve that the pair $(R, W)$ traces in the phase plane, and its direction field shows closed loops around an equilibrium point. Going around a loop, the two populations rise and fall in a cycle, with the predators lagging behind the prey.

## The Lotka–Volterra Equations

Let $R(t)$ be the number of prey (rabbits) and $W(t)$ the number of predators (wolves) at time $t$. Without predators, the ample food supply would support exponential growth of the prey, $dR/dt = kR$ with $k > 0$ ([[§60 Models for Population Growth#^def-60-1|Definition §60.1]], [[§21 Exponential Growth and Decay#^thm-21-1|Theorem §21.1]]). Without prey, the predators would die out at a rate proportional to their number, $dW/dt = -rW$ with $r > 0$. With both present, assume that the main cause of death among the prey is being eaten, and that the birth and survival rates of the predators depend on their food supply, the prey. Assume also that the two species meet at a rate proportional to both populations, that is, to the product $RW$: the more there are of either, the more encounters.

> [!definition] Definition §62.1: The Predator-Prey Equations
> The **predator-prey equations**, or **Lotka–Volterra equations**, are the system
>
> $$
> \frac{dR}{dt} = kR - aRW, \qquad \frac{dW}{dt} = -rW + bRW \qquad (1)
> $$
>
> where $k$, $r$, $a$ and $b$ are positive constants. The term $-aRW$ decreases the natural growth rate of the prey, and the term $bRW$ increases the natural growth rate of the predators.
>
> A **solution** of the system is a pair of functions $R(t)$ and $W(t)$ that satisfy both equations. The system is **coupled**: $R$ and $W$ occur in both equations, so one cannot solve one equation and then the other; they must be solved simultaneously.
>
> *Stewart: 9.6, Equation 1*

^def-62-1

> [!remark]- Connections
> - ODE version: [[§3 Classification of Differential Equations#^def-3-2|331 Def. §3.2]] (systems of differential equations, with the Lotka–Volterra equations as the example) and [[§27 Introduction to Systems of First-Order Linear Equations#^def-27-1|331 Def. §27.1]] (first-order systems, their solutions and initial value problems; a solution traces a trajectory).

Usually it is impossible to find explicit formulas for $R$ and $W$ as functions of $t$, so the equations are analysed graphically. (Volterra proposed them to explain the variations in the shark and food-fish populations of the Adriatic Sea.)

> [!definition] Definition §62.2: Equilibrium Solutions and Equilibrium Points
> The constant solutions of a system such as (1) are its **equilibrium solutions**. They are found by setting both derivatives equal to $0$. The corresponding point $(R, W)$ is an **equilibrium point**.
>
> For (1), $dR/dt = R(k - aW)$ and $dW/dt = W(-r + bR)$ both vanish exactly when $R = W = 0$ or when
>
> $$
> W = \frac{k}{a}, \qquad R = \frac{r}{b} .
> $$
>
> (If $R = 0$ then the second equation forces $W = 0$, and if $W = 0$ the first forces $R = 0$; otherwise both brackets must vanish.)
>
> *Stewart: 9.6 (text; Example 9.6.1)*

^def-62-2

> [!theorem] Proposition §62.1: The Equation of the Phase Trajectories
> Along a solution of (1), at times when $dR/dt \ne 0$, the predator population $W$ can be regarded as a function of the prey population $R$, and it satisfies the first-order differential equation
>
> $$
> \frac{dW}{dR} = \frac{dW/dt}{dR/dt} = \frac{-rW + bRW}{kR - aRW} .
> $$
>
> *Stewart: 9.6 (text; Example 9.6.1(b))*

^prop-62-1

> [!proof]+ Proof
> Let $(R(t), W(t))$ be a solution, and let $t_0$ be a time with $dR/dt \ne 0$. (Stewart applies the Chain Rule directly; here is why $W$ is a function of $R$.) The derivative $dR/dt = kR - aRW$ is continuous, so it keeps its sign on an interval around $t_0$. There $R$ is strictly monotone in $t$ (Increasing/Decreasing Test, [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Theorem §27.1]]), hence one-to-one, and $t$ is a differentiable function of $R$ with $dt/dR = 1/(dR/dt)$ ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|Theorem §19.1]], derivative of an inverse function). So $W = W(t(R))$ is a function of $R$, and by the Chain Rule
>
> $$
> \frac{dW}{dt} = \frac{dW}{dR}\,\frac{dR}{dt} .
> $$
>
> Solving for $dW/dR$ and substituting (1),
>
> $$
> \frac{dW}{dR} = \frac{dW/dt}{dR/dt} = \frac{-rW + bRW}{kR - aRW} .
> $$

^pf-62-1

*Uses:* [[§62 Predator-Prey Systems#^def-62-1|Def. §62.1]], [[§17 The Chain Rule#^thm-17-2|§17.2]] (Chain Rule), [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-1|§19.1]] (derivative of an inverse function), [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|§27.1]] (Increasing/Decreasing Test)

> [!remark]- Connections
> - The local inversion of $t \mapsto R(t)$ where $dR/dt \ne 0$ is the one-variable inverse function theorem, [[§29 The Mean Value Theorem#^thm-29-10|451 Thm. §29.10]].

> [!example] Example §62.1: Rabbits and Wolves — Equilibria and the Direction Field
> Suppose that populations of rabbits and wolves are described by the Lotka–Volterra equations (1) with $k = 0.08$, $a = 0.001$, $r = 0.02$ and $b = 0.00002$, with $t$ in months. (a) Find the equilibrium solutions and interpret the answer. (b) Use the system to find an expression for $dW/dR$. (c) Draw the direction field of the resulting differential equation in the $RW$-plane and use it to sketch some solution curves.
>
> **(a)** The equations are
>
> $$
> \frac{dR}{dt} = 0.08R - 0.001RW, \qquad \frac{dW}{dt} = -0.02W + 0.00002RW .
> $$
>
> Both $R$ and $W$ are constant when both derivatives are $0$:
>
> $$
> R' = R(0.08 - 0.001W) = 0, \qquad W' = W(-0.02 + 0.00002R) = 0 .
> $$
>
> One solution is $R = 0$, $W = 0$: with no rabbits and no wolves, neither population will grow. The other is
>
> $$
> W = \frac{0.08}{0.001} = 80, \qquad R = \frac{0.02}{0.00002} = 1000 .
> $$
>
> So the equilibrium populations are $80$ wolves and $1000$ rabbits: $1000$ rabbits are just enough to support a constant wolf population of $80$. There are neither too many wolves (which would mean fewer rabbits) nor too few (which would mean more rabbits).
>
> **(b)** By Proposition §62.1,
>
> $$
> \frac{dW}{dR} = \frac{dW/dt}{dR/dt} = \frac{-0.02W + 0.00002RW}{0.08R - 0.001RW} .
> $$
>
> **(c)** Regarding $W$ as a function of $R$, this is a first-order differential equation, and its direction field can be drawn as in [[§58 Direction Fields and Euler's Method#^def-58-1|Definition §58.1]]. Its solution curves, sketched from the field (the phase portrait after Example §62.2), appear to be closed: travelling along one, we always return to the starting point. The equilibrium point $(1000, 80)$ lies inside all of them.
>
> *Stewart: Example 9.6.1(a)–(c)*

^ex-62-1

> [!definition] Definition §62.3: Phase Plane, Phase Trajectory, Phase Portrait
> When solutions of a system of differential equations such as (1) are drawn as curves in the $RW$-plane, that plane is called the **phase plane**, and the solution curves are **phase trajectories**. So a phase trajectory is the path traced out by the points $(R(t), W(t))$ as time goes by. A **phase portrait** consists of the equilibrium points together with typical phase trajectories.
>
> *Stewart: 9.6 (text)*

^def-62-3

> [!remark]- Connections
> - ODE version, for linear systems $\mathbf{x}' = A\mathbf{x}$: [[§31 Homogeneous Linear Systems with Constant Coefficients#^def-31-2|331 Def. §31.2]] (phase plane, trajectory, phase portrait), with the possible portraits near the origin classified in [[§32 Complex-Valued Eigenvalues#^thm-32-3|331 Thm. §32.3]].

> [!example] Example §62.2: Rabbits and Wolves — One Cycle
> In the system of Example §62.1, suppose that at some time there are $1000$ rabbits and $40$ wolves. (d) Draw the corresponding solution curve and use it to describe the changes in both populations. (e) Sketch $R$ and $W$ as functions of $t$.
>
> **(d)** We need the phase trajectory through $P_0(1000, 40)$. Which way is it traversed as $t$ increases from $0$? At $P_0$,
>
> $$
> \frac{dR}{dt} = 0.08(1000) - 0.001(1000)(40) = 80 - 40 = 40 > 0 ,
> $$
>
> so $R$ is increasing at $P_0$ and the point moves *counterclockwise* around the trajectory.
>
> At $P_0$ there are not enough wolves to keep the populations in balance, so the rabbits increase. That leads to more wolves, and eventually there are so many wolves that the rabbits have a hard time avoiding them. So the number of rabbits begins to decline, at $P_1$, where $R$ reaches its maximum of about $2800$. At some later time the wolves start to decline, at $P_2$, where $R = 1000$ and $W \approx 140$. This benefits the rabbits, whose number later starts to increase, at $P_3$, where $W = 80$ and $R \approx 210$. Then the wolves eventually increase as well. The populations return to $R = 1000$, $W = 40$, and the cycle begins again.
>
> The positions of the turning points follow from (1). $R$ has a maximum or minimum where $dR/dt = R(0.08 - 0.001W) = 0$, that is, on the line $W = 80$ ($P_1$ and $P_3$); $W$ has one where $dW/dt = 0$, that is, on the line $R = 1000$ ($P_0$ and $P_2$). The values $2800$, $140$ and $210$ are read off the graph; the conserved quantity of the remark below gives $R_{\max} \approx 2803$, $W_{\max} \approx 140.5$ and $R_{\min} \approx 209.5$.
>
> **(e)** Let $P_1$, $P_2$, $P_3$ be reached at times $t_1$, $t_2$, $t_3$. From the description in (d), $R$ rises from $1000$ to its peak at $t_1$, falls to its minimum at $t_3$ and climbs back; $W$ rises from $40$ to its peak at $t_2$, falls, and returns to $40$. Both graphs are periodic, with the period of one trip around the trajectory. Drawn on the same axes with different scales, they show the rabbits peaking before the wolves (second figure below; Stewart describes the lag as about a quarter of a cycle).
>
> *Stewart: Example 9.6.1(d)–(e)*

^ex-62-2

![[m233-62-1.svg]]
*Phase portrait of the rabbit–wolf system of Examples §62.1 and §62.2. The grey arrows show the direction of $(dR/dt, dW/dt)$, so they give the direction field of $dW/dR$ and the sense of travel. The red trajectory through $P_0(1000, 40)$ is traversed counterclockwise; $R$ turns at $P_1$ and $P_3$ on the line $W = 80$, and $W$ turns at $P_2$ and $P_0$ on the line $R = 1000$. Two smaller trajectories (blue) circle the equilibrium point $(1000, 80)$ as well.*

![[m233-62-2.svg]]
*$R(t)$ (blue, left scale) and $W(t)$ (red, right scale) for the solution with $R(0) = 1000$, $W(0) = 40$, computed numerically. One cycle takes about $T \approx 170$ months. The rabbits peak at $t_1 \approx 36$, the wolves at $t_2 \approx 63$, and the rabbits bottom out at $t_3 \approx 110$. The wolf peak trails the rabbit peak by about $27$ months, and the wolf minimum trails the rabbit minimum by about $60$ months; on average the lag is about a quarter cycle.*

> [!remark]- Remark: Why the Trajectories Are Closed
> Stewart observes that the trajectories *appear* closed. His Exercise 9.6.9 gives the reason. The equation of Proposition §62.1 is separable ([[§59 Separable Equations#^def-59-1|Definition §59.1]]; solved by [[§59 Separable Equations#^thm-59-1|Theorem §59.1]]):
>
> $$
> \frac{dW}{dR} = \frac{W(-r + bR)}{R(k - aW)} \quad\Longrightarrow\quad \int \frac{k - aW}{W}\,dW = \int \frac{-r + bR}{R}\,dR ,
> $$
>
> so $k\ln W - aW = -r\ln R + bR + \text{const}$ (with $R, W > 0$). In other words, the function
>
> $$
> H(R, W) = r\ln R - bR + k\ln W - aW
> $$
>
> is constant along every phase trajectory. This can be checked directly, even where $dR/dt = 0$: by the Chain Rule and (1),
>
> $$
> \frac{d}{dt}H(R, W) = \Big(\frac{r}{R} - b\Big)R(k - aW) + \Big(\frac{k}{W} - a\Big)W(-r + bR) = (r - bR)(k - aW) - (k - aW)(r - bR) = 0 .
> $$
>
> For the numbers of Example §62.1, exponentiating $H = \text{const}$ gives Stewart's form $\dfrac{R^{0.02}\,W^{0.08}}{e^{0.00002R}\,e^{0.001W}} = C$.
>
> The function $r\ln R - bR$ increases for $R < r/b$, decreases for $R > r/b$, and tends to $-\infty$ as $R \to 0^+$ and as $R \to \infty$; the same holds for $k\ln W - aW$ about $W = k/a$. So $H$ has a single peak, at the equilibrium point $(r/b, k/a)$, and falls off in every direction. Its level curves $H = C$ (for $C$ below the peak value) are therefore closed loops around the equilibrium. A solution starting on such a loop stays on it. The loop contains no equilibrium point, so the speed $\sqrt{(dR/dt)^2 + (dW/dt)^2}$ is bounded below by a positive number on it (a continuous positive function on a closed bounded set), and the solution travels all the way around the loop in a finite time. This is why the populations are periodic. The level curve cannot be solved for $W$ as an explicit function of $R$ (or vice versa); it is defined implicitly.

^rem-62-1

> [!remark]- Connections
> - Near each point where $\partial H/\partial W \ne 0$ (that is, $W \ne k/a$), the implicit function theorem solves $H(R, W) = C$ for $W$ as a differentiable function of $R$, with $dW/dR = -H_R/H_W$, which is again the equation of Proposition §62.1: [[§12 The Implicit Function Theorem#^thm-12-1|452 Thm. §12.1]].

## Testing and Extending the Model

> [!remark]- Remark: Hares and Lynx
> Part of modelling is to test predictions against real data. The Hudson's Bay Company, trading in animal furs in Canada since 1670, has records going back to the 1840s. The numbers of pelts of the snowshoe hare and of its predator, the Canada lynx, traded over a 90-year period show the coupled oscillations predicted by the Lotka–Volterra model, with a period of roughly 10 years.

^rem-62-2

The simple model has had some success in explaining and predicting coupled populations, but more refined models have also been proposed.

> [!definition] Definition §62.4: Predator-Prey Equations with Logistic Prey
> If, in the absence of predators, the prey grow according to the logistic model with carrying capacity $M$ ([[§60 Models for Population Growth#^def-60-2|Definition §60.2]]), the Lotka–Volterra equations (1) are replaced by
>
> $$
> \frac{dR}{dt} = kR\Big(1 - \frac{R}{M}\Big) - aRW, \qquad \frac{dW}{dt} = -rW + bRW .
> $$
>
> *Stewart: 9.6 (text)*

^def-62-4

With limited food for the prey, the trajectories are no longer closed: in Stewart's Exercise 9.6.11 the trajectory through $(1000, 40)$ spirals in toward an equilibrium point. Similar systems model two or more species that compete for the same resources, or that cooperate for mutual benefit (flowering plants and insect pollinators); there the interaction terms in both equations have the same sign.
