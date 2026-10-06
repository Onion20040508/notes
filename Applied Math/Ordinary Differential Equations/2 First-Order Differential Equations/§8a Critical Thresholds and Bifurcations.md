---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 8
bdp: "2.5"
aliases: ["BDP 2.5 (cont.)"]
tags: [ordinary-differential-equations, math331]
---
← [[§8 Autonomous Differential Equations and Population Dynamics]] · ↑ [[· 2 First-Order Differential Equations]] · [[§9 Exact Differential Equations and Integrating Factors]] →

*Boyce–DiPrima, Section 2.5 · MATH 331 Written HW 2 (Problem 2), Midterm (Fall 2021) Q5, Midterm (Spring 2020) Q6.*

The second half of BDP 2.5, continuing [[§8 Autonomous Differential Equations and Population Dynamics|§8]]: the qualitative picture of an autonomous equation is developed on growth with a critical threshold and on a combination of the threshold with logistic growth, and then on equations with a parameter, whose critical points can merge or split at bifurcation points. Equation numbers continue those of [[§8 Autonomous Differential Equations and Population Dynamics|§8]].

## A Critical Threshold

Changing the sign of the right side of the logistic equation changes the behaviour completely. Consider

$$
\frac{dy}{dt} = -r\Big(1 - \frac yT\Big)y , \qquad (14)
$$

with positive constants $r$ and $T$. The graph of $f(y)$ is now a downward-shifted parabola through the critical points $y = 0$ and $y = T$, with vertex $(T/2, -rT/4)$. If $0 < y < T$ then $dy/dt < 0$ and $y$ decreases, so $\phi_1(t) = 0$ is asymptotically stable; if $y > T$ then $dy/dt > 0$ and $y$ increases, so $\phi_2(t) = T$ is unstable. By [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-2|Proposition §8.2]], $f'(y) < 0$ for $0 < y < T/2$ and $f'(y) > 0$ for $T/2 < y < T$, so solutions in the strip $0 < y < T$ are concave up below $T/2$ and concave down above it; for $y > T$ both $f$ and $f'$ are positive, and solutions are concave up. The solutions in $0 < y < T$ decrease to $0$; those above $T$ increase more and more steeply.

> [!definition] Definition §8.8: Threshold Level
> In equation (14) the value $T$ is a **threshold level**: if the initial value $y_0$ is less than $T$, the solution approaches zero as $t$ increases, and if $y_0 > T$ it grows without bound. Below the threshold, growth does not occur.
>
> *BDP: 2.5 (text)*

^def-8-8

> [!remark]- Connections
> - Stewart's versions of a threshold (a minimum viable population) and of harvesting, as modifications of the logistic equation: [[§60 Models for Population Growth#^def-60-new1|Calc Def. §60.4]] (minimum population) and [[§60 Models for Population Growth#^def-60-new1|Calc Def. §60.4]] (minimum population) and [[§60 Models for Population Growth#^def-60-3|Calc Def. §60.3]] (harvesting) (harvesting).

> [!theorem] Proposition §8.6: Solution of the Threshold Equation
> The solution of (14) with $y(0) = y_0 > 0$ is
>
> $$
> y = \frac{y_0 T}{y_0 + (T - y_0)e^{rt}} . \qquad (15)
> $$
>
> If $0 < y_0 < T$, then $y \to 0$ as $t \to \infty$. If $y_0 > T$, the denominator vanishes at
>
> $$
> t^* = \frac1r \ln \frac{y_0}{y_0 - T} , \qquad (16)
> $$
>
> and the solution has a vertical asymptote there: the population becomes unbounded in finite time.
>
> *BDP: 2.5, equations (15) and (16)*

^prop-8-6

> [!proof]+ Proof
> Equation (14) is (7) with $K$ replaced by $T$ and $r$ by $-r$, and the derivation of [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|Proposition §8.3]] did not use the sign of $r$; making the same replacements in (11) gives (15). To check it directly, let $D(t) = y_0 + (T - y_0)e^{rt}$, so $y = y_0T/D$ and $D - y_0 = (T - y_0)e^{rt}$. Then
>
> $$
> y' = -\frac{y_0T\,D'}{D^2} = -\frac{y_0T\,r(T - y_0)e^{rt}}{D^2}, \qquad
> -r\Big(1 - \frac yT\Big)y = -r\,\frac{D - y_0}{D}\,\frac{y_0T}{D} = -\frac{r\,(T - y_0)e^{rt}\,y_0T}{D^2} ,
> $$
>
> which agree, and $y(0) = y_0T/T = y_0$. By the uniqueness part of Theorem 2.4.2 ([[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]]) this is the solution as long as $D \ne 0$.
>
> If $0 < y_0 < T$, then $D(t) \ge y_0 > 0$ for $t \ge 0$ and $D(t) \to \infty$, so $y \to 0$. If $y_0 > T$, then $D(t) = y_0 - (y_0 - T)e^{rt}$ decreases from $y_0$ and vanishes when $e^{rt^*} = y_0/(y_0 - T)$, which is (16); since $y_0/(y_0 - T) > 1$, $t^* > 0$. As $t \to t^{*-}$, $D \to 0^+$ and $y \to +\infty$. (BDP leaves (16) as Problem 12.)

^pf-8-6

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|§8.3]], [[§11 The Existence and Uniqueness Theorem#^thm-11-8|§11.8]] (uniqueness)

*Forward reference: [[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]] (BDP Theorem 2.4.2) is proved later, in [[§11 The Existence and Uniqueness Theorem|§11]] (BDP 2.8).*

The existence and location of this asymptote were not visible in the geometric analysis: here the explicit solution adds qualitative as well as quantitative information. Some species show the threshold phenomenon: if too few are present, the species cannot propagate itself successfully and becomes extinct, while above the threshold the population grows. In fluid mechanics, equations of the form (7) or (14) govern a small disturbance $y$ of a laminar flow; under (14) a disturbance below the *critical amplitude* $T$ is damped out, and one above it grows and the flow becomes turbulent.

## Logistic Growth with a Threshold

Unbounded growth is unrealistic, so (14) is modified by a factor that makes $dy/dt$ negative when $y$ is large:

$$
\frac{dy}{dt} = -r\Big(1 - \frac yT\Big)\Big(1 - \frac yK\Big)y , \qquad r > 0,\ 0 < T < K . \qquad (17)
$$

There are three critical points, $y = 0$, $y = T$ and $y = K$, giving the equilibrium solutions $\phi_1(t) = 0$, $\phi_2(t) = T$, $\phi_3(t) = K$. From the graph of $f$: $dy/dt > 0$ for $T < y < K$, and $dy/dt < 0$ for $y < T$ and for $y > K$. So $\phi_1 = 0$ and $\phi_3 = K$ are asymptotically stable and $\phi_2 = T$ is unstable. A population starting below the threshold $T$ declines to extinction; one starting above $T$ approaches the carrying capacity $K$. A model of this sort apparently describes the passenger pigeon, which could breed successfully only in large concentrations: by the late 1880s too few remained in any one place, and the species died out (the last one in 1914).

> [!theorem] Proposition §8.7: Inflection Points for Logistic Growth with a Threshold
> The inflection points of the solutions of (17) lie on the lines $y = y_1$ and $y = y_2$, where
>
> $$
> y_{1,2} = \frac{K + T \pm \sqrt{K^2 - KT + T^2}}{3} , \qquad (18)
> $$
>
> the plus sign giving $y_1$ and the minus sign $y_2$. These are the maximum point $y_1 \in (T, K)$ and the minimum point $y_2 \in (0, T)$ of $f(y)$.
>
> *BDP: 2.5, equation (18)*

^prop-8-7

> [!proof]+ Proof
> Expanding, $f(y) = -r\Big(y - \Big(\dfrac1T + \dfrac1K\Big)y^2 + \dfrac{y^3}{TK}\Big)$, so
>
> $$
> f'(y) = -r\Big(1 - \frac{2(T + K)}{TK}\,y + \frac{3y^2}{TK}\Big) = -\frac{r}{TK}\big(3y^2 - 2(K + T)y + KT\big) .
> $$
>
> By the quadratic formula $f'(y) = 0$ at $y = \big(2(K + T) \pm \sqrt{4(K + T)^2 - 12KT}\big)/6$, which simplifies to (18) because $(K + T)^2 - 3KT = K^2 - KT + T^2 > 0$. These are simple roots, so $f'$ changes sign at each of them; since $f(y) \ne 0$ there (by Rolle's theorem $f'$ has one root in $(0, T)$ and one in $(T, K)$, and these are the only two), $y'' = f'(y)f(y)$ changes sign exactly when a solution crosses $y = y_1$ or $y = y_2$ ([[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-2|Proposition §8.2]]). (BDP leaves the computation as Problem 13.)

^pf-8-7

*Uses:* [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-2|§8.2]], [[§29 The Mean Value Theorem#^thm-29-2|451 Thm. §29.2]] (Rolle's theorem)

> [!example] Example §8.3: Phase Lines with a Threshold
> **(a)** A population of squirrels $P(t)$ ($t$ in years) satisfies
>
> $$
> \frac{dP}{dt} = 2P\Big(1 - \frac P2\Big)(P - 1) .
> $$
>
> Find all equilibrium points, draw the phase line and determine the stability of each. Graph the solutions with $P(0) = \frac18$, $P(0) = 1.5$ and $P(0) = 2.5$.
>
> **Equilibria.** $f(P) = 0$ when $P = 0$, $P = 2$ or $P = 1$.
>
> **Signs.** Tabulate the signs of the factors $2P$, $1 - P/2$ and $P - 1$:
>
> | interval | $2P$ | $1 - P/2$ | $P - 1$ | $f(P)$ | $P(t)$ |
> |---|---|---|---|---|---|
> | $P < 0$ | $-$ | $+$ | $-$ | $+$ | increasing |
> | $0 < P < 1$ | $+$ | $+$ | $-$ | $-$ | decreasing |
> | $1 < P < 2$ | $+$ | $+$ | $+$ | $+$ | increasing |
> | $P > 2$ | $+$ | $-$ | $+$ | $-$ | decreasing |
>
> **Classification.** The arrows point toward $P = 0$ from both sides and toward $P = 2$ from both sides, and away from $P = 1$ on both sides: $P = 0$ and $P = 2$ are asymptotically stable, $P = 1$ is unstable. The derivative test agrees: $f(P) = -P^3 + 3P^2 - 2P$, $f'(P) = -3P^2 + 6P - 2$, and $f'(0) = -2 < 0$, $f'(1) = 1 > 0$, $f'(2) = -2 < 0$.
>
> This is equation (17) with $r = 2$, threshold $T = 1$ and carrying capacity $K = 2$: indeed $-2(1 - P)(1 - P/2)P = 2P(1 - P/2)(P - 1)$. Squirrels below the threshold $1$ die out; above it they approach $2$.
>
> **The three solutions** (figure below). By (18) the inflection lines are $y_{1,2} = \big(3 \pm \sqrt{3}\big)/3 = 1 \pm 1/\sqrt3$, about $1.577$ and $0.423$.
> - $P(0) = \frac18$: below the threshold, so $P$ decreases to $0$; since $\frac18 < 0.423$, it is concave up throughout.
> - $P(0) = 1.5$: between $T = 1$ and $K = 2$, so $P$ increases to $2$; it starts concave up (below $1.577$) and has an inflection point where it crosses $P \approx 1.577$, then flattens toward $2$.
> - $P(0) = 2.5$: above $K$, so $P$ decreases to $2$, concave up.
>
> **(b)** A colony of quokka (in hundreds; $t$ in years) satisfies $\dfrac{dP}{dt} = 3P\Big(1 - \dfrac P3\Big)(P - 1)$. Draw the phase line and classify the equilibria; if $P(0) = P_0$, find all $P_0$ for which $\lim_{t \to \infty} P(t) > 0$.
>
> The same sign table, with $1 - P/3$ in place of $1 - P/2$, gives equilibria $0$ (asymptotically stable), $1$ (unstable) and $3$ (asymptotically stable): equation (17) with $r = 3$, $T = 1$, $K = 3$. A solution with $0 \le P_0 < 1$ decreases to $0$; $P_0 = 1$ stays at $1$; and $P_0 > 1$ gives $P(t) \to 3$. (Negative $P_0$ are not populations; those solutions increase to $0$.) So
>
> $$
> \lim_{t \to \infty} P(t) > 0 \iff P_0 \ge 1 .
> $$
>
> The equilibrium value $P_0 = 1$ belongs to the answer, although it is unstable: the limit of the constant solution is $1 > 0$.
>
> *Source: 331 Written HW 2, Problem 2(a)(b); 331 Midterm (Fall 2021), Q5*

^ex-8-3

![[m331-8-1.svg]]
*The squirrel equation $P' = 2P(1 - P/2)(P - 1)$ of [[§8a Critical Thresholds and Bifurcations#^ex-8-3|Example §8.3]](a). Left, the phase line: arrows point toward the stable equilibria $0$ and $2$ (green) and away from the unstable threshold $1$ (red). Right, solutions in the $tP$-plane: below the threshold (blue) they decay to $0$, above it (orange) they approach the carrying capacity $2$, never crossing the equilibrium lines. Solutions change concavity on the dashed lines $y_{1,2} = 1 \pm 1/\sqrt3$ of [[§8a Critical Thresholds and Bifurcations#^prop-8-7|Proposition §8.7]].*

## Bifurcation Points

When the right side depends on a parameter $a$, the critical points move as $a$ varies, and at special values of $a$ they can merge or split.

> [!definition] Definition §8.9: Bifurcation Point
> For an equation
>
> $$
> \frac{dy}{dt} = f(a, y) ,
> $$
>
> where $a$ is a real parameter, the critical points usually depend on $a$. A value of $a$ at which critical points come together or separate, so that equilibrium solutions are lost or gained, is called a **bifurcation point**. Three standard types:
> - **saddle–node bifurcation**: two critical points merge and disappear, as for $y' = a - y^2$ at $a = 0$ (no critical points for $a < 0$, the semistable point $0$ for $a = 0$, the points $\pm\sqrt a$ for $a > 0$);
> - **pitchfork bifurcation**: one critical point splits into three, as for $y' = ay - y^3$ at $a = 0$;
> - **transcritical bifurcation**: two critical points cross and **exchange stability**, as for $y' = ay - y^2$ at $a = 0$ (for $a < 0$, $y = 0$ is asymptotically stable and $y = a$ unstable; for $a > 0$ the reverse).
>
> *BDP: 2.5, Problems ("Bifurcation Points"; Problems 2.5.24–26 and their notes)*

^def-8-9

> [!definition] Definition §8.9: Bifurcation Diagram
> For an equation $dy/dt = f(a, y)$ with a real parameter $a$, the plot of the critical points as functions of $a$, in the $ay$-plane, is the **bifurcation diagram**.
>
> *BDP: 2.5, Problems ("Bifurcation Points"; Problems 2.5.24–26 and their notes)*

^def-8-new1

> [!example] Example §8.4: Harvesting Squirrels
> In [[§8a Critical Thresholds and Bifurcations#^ex-8-3|Example §8.3]](a), hunting is permitted: a fraction $\alpha$ of the squirrel population may be eliminated every year, so
>
> $$
> \frac{dP}{dt} = 2P\Big(1 - \frac P2\Big)(P - 1) - \alpha P , \qquad \alpha \ge 0 .
> $$
>
> One association asserts that no more than $20\%$ may be eliminated ($\alpha = 0.2$), otherwise the population goes extinct; another asserts that $40\%$ ($\alpha = 0.4$) is safe. Analyze the equation as $\alpha$ varies, decide who is right, and find the largest $\alpha$ for which the population does not go extinct.
>
> **Factor.** $2P(1 - P/2)(P - 1) = P(2 - P)(P - 1) = P(-P^2 + 3P - 2)$, so
>
> $$
> f_\alpha(P) = P(-P^2 + 3P - 2 - \alpha) = -P\,(P^2 - 3P + 2 + \alpha) .
> $$
>
> **Critical points.** $P = 0$, and the roots of $P^2 - 3P + 2 + \alpha = 0$. Completing the square, $\big(P - \frac32\big)^2 = \frac94 - 2 - \alpha = \frac14 - \alpha$, so
>
> $$
> P_\pm = \frac32 \pm \sqrt{\tfrac14 - \alpha} \qquad (\alpha \le \tfrac14) .
> $$
>
> **Case $0 \le \alpha < \frac14$.** Three critical points $0 < P_- < P_+$ (note $P_- \ge 1 > 0$), and $f_\alpha(P) = -P(P - P_-)(P - P_+)$. For $0 < P < P_-$, $f_\alpha < 0$; for $P_- < P < P_+$, $f_\alpha > 0$; for $P > P_+$, $f_\alpha < 0$. So $P = 0$ is asymptotically stable, $P_-$ is an unstable threshold and $P_+$ an asymptotically stable carrying capacity. The population survives (approaches $P_+$) exactly when $P(0) > P_-$. At $\alpha = 0$ this is [[§8a Critical Thresholds and Bifurcations#^ex-8-3|Example §8.3]] ($P_- = 1$, $P_+ = 2$); as $\alpha$ grows the threshold rises and the carrying capacity falls.
>
> **Case $\alpha = \frac14$.** $f_{1/4}(P) = -P\big(P - \frac32\big)^2 \le 0$ for $P \ge 0$, with a double root at $\frac32$. Solutions above $\frac32$ decrease to $\frac32$, solutions below it decrease to $0$: $P = \frac32$ is semistable ([[§8 Autonomous Differential Equations and Population Dynamics#^def-8-7|Definition §8.7]]).
>
> **Case $\alpha > \frac14$.** The quadratic $P^2 - 3P + 2 + \alpha$ has discriminant $9 - 4(2 + \alpha) = 1 - 4\alpha < 0$, so it is positive for all $P$, and $f_\alpha(P) < 0$ for every $P > 0$. The only critical point is $0$: every positive solution decreases, and by [[§8 Autonomous Differential Equations and Population Dynamics#^lem-8-4|Lemma §8.4]] it tends to $0$. The population goes extinct, whatever its size.
>
> **Answer.** $\alpha = \frac14$ is a bifurcation point (a saddle–node: the threshold and the carrying capacity merge at $\frac32$ and disappear). With $\alpha = 0.2$ there are equilibria $P_\pm = 1.5 \pm \sqrt{0.05} \approx 1.276$ and $1.724$, so a population above about $1.276$ survives and settles near $1.724$. With $\alpha = 0.4 > \frac14$ the population goes extinct. So the hunters (40%) are wrong, and hunting 20% is safe as the conservationists say; but their claim that more than 20% leads to extinction is too strong. The largest rate is
>
> $$
> \alpha_{\max} = \tfrac14 = 25\% ,
> $$
>
> at which a population starting at or above $\frac32$ still survives (tending to $\frac32$); for every $\alpha > \frac14$ extinction is certain. A harvest proportional to the population, as here, is the setting of the Schaefer model of fisheries (BDP Problem 2.5.19).
>
> *Source: 331 Written HW 2, Problem 2(c)*

^ex-8-4

![[m331-8-2.svg]]
*Bifurcation diagram of [[§8a Critical Thresholds and Bifurcations#^ex-8-4|Example §8.4]]: the critical points of $P' = 2P(1 - P/2)(P - 1) - \alpha P$ against the harvesting rate $\alpha$. Solid curves are asymptotically stable, the dashed one unstable. The threshold $P_-$ and the carrying capacity $P_+$ approach each other as $\alpha$ grows and merge at the semistable point $(\frac14, \frac32)$; beyond it (shaded) only $P = 0$ is left. The rate $\alpha = 0.2$ lies to the left of the bifurcation, $\alpha = 0.4$ to the right.*
